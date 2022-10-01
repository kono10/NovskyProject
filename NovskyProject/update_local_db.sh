export DJANGO_ENV=PROD
echo DUMPING DATA ...
python manage.py dumpdata -e contenttypes -e admin -e auth --indent 2 > fixtures/db.json
export DJANGO_ENV=DEV
echo LOADING DATA ...
python manage.py loaddata fixtures/db.json
