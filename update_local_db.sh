# need to have a virtual env set up, install packages using requirements.txt
export DJANGO_ENV=PROD
echo DUMPING DATA INTO LOCAL fixtures/db.json...
python NovskyProject/manage.py dumpdata -e contenttypes -e admin -e auth --indent 2 > NovskyProject/visuals/fixtures/db.json
export DJANGO_ENV=DEV
echo LOADING DATA DATA FROM fixutres/db.json into local sql lite db ...
python NovskyProject/manage.py makemigrations
python NovskyProject/manage.py migrate
python NovskyProject/manage.py loaddata NovskyProject/visuals/fixtures/db.json
