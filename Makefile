SITE_SOURCE_DIR ?= .
SITE_BUILD_DIR ?= _site
APP_DIR ?= app
APP_NAME= ?= oxford-invariants
APP_NAME_STAGING ?= oxford-invariants-staging
VERSION = 2017-03

all: build

build:
	jekyll build --source $(SITE_SOURCE_DIR) --destination $(SITE_BUILD_DIR)
	mv $(SITE_BUILD_DIR)/contact/index.html $(APP_DIR)/contact.html
	rmdir $(SITE_BUILD_DIR)/contact/
	rm -rf $(APP_DIR)/www
	cp -r $(SITE_BUILD_DIR) $(APP_DIR)/www

deploy: build
	gcloud config set project $(APP_NAME)
	gcloud app deploy $(APP_DIR)/app_production.yaml --version="$(VERSION)" --promote
	gcloud config unset project

stage: build
	gcloud config set project $(APP_NAME_STAGING)
	gcloud config set app/promote_by_default false
	gcloud app deploy $(APP_DIR)/app_staging.yaml --version=$(shell git rev-parse --abbrev-ref HEAD)
	gcloud config unset project
	gcloud config unset app/promote_by_default

test: build
	dev_appserver.py $(APP_DIR)/app_production.yaml

clean:
	rm -rf $(SITE_BUILD_DIR)/*
