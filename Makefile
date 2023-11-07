clean:
	rm -rf build/
	rm -rf computations_files/
	rm -rf _freeze
	rm -rf .venv
	rm -rf .ipynb_checkpoints
	
build: venv extensions
	poetry run quarto render .

venv:
	poetry install

extensions:
	quarto add quarto-ext/lightbox --no-prompt