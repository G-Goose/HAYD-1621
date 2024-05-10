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

run_loading_model:
	python -c 'from hayd1621.model import run_loading_model; loading_model()'

run_input_process:
	python -c

all: install clean

gar_creation:
	gcloud auth configure-docker ${GCP_REGION}-docker.pkg.dev
	gcloud artifacts repositories create ${GAR_REPO} --repository-format=docker \
	--location=${GCP_REGION} --description="Repository for storing ${GAR_REPO} images"

docker_build:
	docker build --platform linux/amd64 -t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod .

docker_build_m2:
	docker build --platform linux/arm64 -t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:m2 .

docker_push:
	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod

docker_run:
	docker run -e PORT=8000 -p 8000:8000 --env-file .env ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod

docker_run_m2:
	docker run -e PORT=8000 -p 8000:8000 --env-file .env ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:m2

docker_interactive:
	docker run -it --env-file .env ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod /bin/bash

docker_deploy:
	gcloud run deploy --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GAR_REPO}/${GAR_IMAGE}:prod --memory ${GAR_MEMORY} --region ${GCP_REGION} --env-vars-file .env.yaml
