install:
	@pip install -e .

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -Rf */.ipynb_checkpoints
	@rm -Rf build
	@rm -Rf */__pycache__
	@rm -Rf */*.pyc

run_api:
  uvicorn api.fast:app --reload

all: install clean
