FROM python:3.6
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV DJANGO_ENV=PROD
COPY . .

CMD ["gunicorn", "--bind"," 0.0.0.0:8000", "--workers=4", "myproject.wsgi:application"]
