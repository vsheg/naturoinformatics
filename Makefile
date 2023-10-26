clean:
	rm -rf build/
	rm -rf computations_files/
	rm -rf _freeze
	
build: venv
	poetry run quarto render .

venv:
	poetry install

extensions:
	quarto add quarto-ext/lightbox --no-prompt