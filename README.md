### Django Resources
* https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/#configuring-a-database
* https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
* https://medium.com/analytics-vidhya/creating-a-django-ci-cd-pipeline-with-travis-ci-and-aws-elasticbeanstalk-b91bfedd144c
* https://django.how/resources/aws-rds-postgresql-instance-for-django-project/
* https://levelup.gitconnected.com/how-to-implement-login-logout-and-registration-with-djangos-user-model-59442164db73
* https://realpython.com/intro-to-pyenv/

### Development Setup Instructions
____

Install pip
`apt install python3-pip`

Install vitualenv
`pip3 install virtualenv`

Create a virtual environment
`virtualenv djangoEnv -p python3`

Create a python 3.6 env
`virtualenv --python=python3.6 myvenv`

Activate the environment
`source djangoEnv/bin/activate`
 
Install Django
`pip install django`
 
Setup Django Db
`cd jake_project/jake_project/`
`python manage.py migrate`
 
Create A User
`python manage.py createsuperuser`

## Start up production server (uses gunicorn and nginx) build and run docker containers locally
* can add -D or --daemon command to the below to run in the background
* accessed from localhost
```
❯ docker compose -f docker-compose.yml up --build
```

## Start up local django dev server with local buids, visit at localhost:8005
```
❯ docker-compose -f docker-compose-test-project.yml up --build  
```
## Run Test in Docker Env 
```
❯ docker compose -f docker-compose-run-test-locally.yml up --build
```
* eliminates the need to have a remote db connection or a python virtualenv
* if you do want to run tests with the remote prod db just update DJANGO_ENV to PROD in docker-compose-run-test-locally.ym

### File Index
* update_local_db.sh -> must have PG_PASSWORD, PG_URL in ENV variables, will take db data from remote db and store it locally to be used for unit tests running tests locally
* docker-compose-run-test-locally.yml -> will run unit tests in django locally in a docker environment, is convenient bc you don't need a python virtualenv
* docker-compose-test-app.yml -> run django dev server (python manage.py runserver) in docker env (i.e. without a python virtualenv) using the remote db or a local sql lite db, depending on the DJANGO_ENV
* docker-compose-dev-app.yml -> test production infrastructure with local docker builds
* docker-compose.yml -> can run production infrastructure locally (pulls images dockerhub), is the compose file used by AWS
