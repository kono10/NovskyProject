export DJANGO_ENV=PROD
echo DUMPING DATA ...
python NovskyProject/manage.py dumpdata -e contenttypes -e admin -e auth --indent 2 > fixtures/db.json
export DJANGO_ENV=DEV
echo LOADING DATA ...
python NovskyProject/manage.py makemigrations
python NovskyProject/manage.py migrate
python NovskyProject/manage.py loaddata NovskyProject/visuals/fixtures/db.json
