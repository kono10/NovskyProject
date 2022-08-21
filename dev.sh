#! /bin/bash
python myproject/manage.py collectstatic
docker-compose -f docker-compose-dev.yml up --build
