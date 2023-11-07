# main rules

clean:
	rm -rf render/
	rm -rf computations_files/
	rm -rf _freeze
	rm -rf .venv
	rm -rf .ipynb_checkpoints

render:
	poetry run quarto render .

environment: python_env quarto_env

# helper rules

python_env:
	poetry install

quarto_env:
	quarto add quarto-ext/lightbox --no-prompt