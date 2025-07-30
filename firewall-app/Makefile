# Makefile for building and deploying to Google Cloud Run

PROJECT_ID ?= torch-3
SERVICE ?= firewall-login
REGION ?= us-east1
IMAGE ?= $(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(SERVICE)-repo/$(SERVICE)
PORT ?= 8080

.PHONY: all build push deploy run local

build:
	docker build -t $(IMAGE) .
#	gcloud builds submit --tag $(IMAGE)

# Did this first:
# gcloud auth configure-docker us-east1-docker.pkg.dev
# gcloud artifacts repositories create firewall-login-repo --repository-format=docker --location=us-east1
push: build
	docker push ${IMAGE}

deploy:
	gcloud run deploy $(SERVICE) \
	  --image $(IMAGE) \
	  --platform managed \
	  --region $(REGION) \
	  --allow-unauthenticated \
	  --set-env-vars SECRET_KEY=359bynpq3a9tynbqap39tyn4

run: build
	docker run --rm -p $(PORT):8080 $(IMAGE)
