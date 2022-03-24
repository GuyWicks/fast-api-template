serve:
	pipenv shell mkdocs serve

build: deploy
deploy: 
	pipenv shell mkdocs gh-deploy

run:
	pipenv run uvicorn app.main:app --reload 
#--reload-delay 10.0 --workers=1

install:
	pipenv install --dev
#	pipenv install mkdocs
#	pipenv install mkdocs-material

upgrade: update

update: 
	pipenv update
#	pipenv update mkdocs
#	pipenv update mkdocs-material
