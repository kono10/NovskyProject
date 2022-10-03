FROM python:3.6
# TODO change this to django_project
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind"," 0.0.0.0:8000", "--workers=4", "NovskyProject.wsgi:application"]
