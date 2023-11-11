# main rules

clean:
	rm -rf computations_files/
	rm -rf .venv/
	rm -rf .ipynb_checkpoints/
	rm -rf _site/
	rm -rf _freeze/
	rm -rf _extensions/

render:
	poetry run quarto render .

env: python_env quarto_env

# helper rules

python_env:
	poetry install

quarto_env:
	quarto add quarto-ext/lightbox --no-prompt

.PHONY: render clean