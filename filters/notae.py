from typing import Any, Optional
from pprint import PrettyPrinter
from httpcore import stream
from panflute import *
from sys import stderr
from typing import Collection

DEF_OPERATOR = ':-'
RE_OPERATOR = ':='
NOTAE_DIV_CLASS = 'notae'

pp = PrettyPrinter(stream=stderr)


def split_by(list_: list, sep: Any) -> list:
    '''Splits list into sublists by delimiter.'''

    match sep:
        case [*_]:
            pass
        case _:
            sep = [sep]

    result = [[]]

    for el in list_:
        if el not in sep:
            result[-1].append(el)
        else:
            result.append([])

    return result


def parse_line(line: list) -> Optional[DefinitionItem]:
    '''Finds definition syntax and returns definition object or `None`.'''

    splitted = split_by(line, [Str(DEF_OPERATOR), Str(RE_OPERATOR)])

    if len(splitted) != 2:
        return None

    term, def_ = splitted
    def_ = Definition(Plain(*def_))

    return DefinitionItem(term, [def_])


def parse_para(para: Para, _: Any) -> Optional[list]:

    if not isinstance(para, Para):
        return None

    blocks = [[]]

    lines = split_by(para.content, SoftBreak())

    for line in lines:
        if def_ := parse_line(line):
            blocks[-1].append(def_)
        else:
            blocks.append(Plain(*line))
            blocks.append([])

    def filter_(item: list) -> Any:
        match item:
            case []:
                return Plain(LineBreak())
            case list():
                return DefinitionList(*item)
            case Plain():
                return item

    blocks = [filter_(el) for el in blocks]  # remove empty lists

    # pp.pprint(blocks)
    return blocks


def action(div, doc) -> None:
    match div:
        case Div() if NOTAE_DIV_CLASS in div.classes:
            div.walk(parse_para)


run_filter(action)
