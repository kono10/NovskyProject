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

Activate the environment
`source djangoEnv/bin/activate`
 
Install Django
`pip install django`
 
Setup Django Db
`cd jake_project/jake_project/`
`python manage.py migrate`
 
Create A User
`python manage.py createsuperuser`


## Start up the django docker development server for local testing
* accessed from localhost:8001
```
❯ pwd
~/DjangoElasticBeanstalkTemplate/myproject

❯ docker build -f Dockerfile.dev -t djangodev .

❯ docker run -p 8001:8000 djangodev
```

## Start up production server (uses gunicorn and nginx) build and run docker containers locally
* can add -D or --daemon command to the below to run in the background
* accessed from localhost:4005
* use `dev.sh` so you don't have to run `python myproject/manage.py collecstatic` manually

```
❯ pwd
~/DjangoElasticBeanstalkTemplate

❯ docker-compose -f docker-compose-dev.yml up --build  
```

## Start up local django dev server, visit at localhost:8005



### File Index
* docker-compose-test.yml -> run django dev server
* docker-compose-dev.yml -> test production infrastructure with local docker builds
* docker-compose.yml -> can run production infrastructure locally but pulls docker containers from dockerhub, is the compose file used by AWS
* Dockerfile.dev -> run Django app locally with Django development server
