FROM python:3.7
WORKDIR /app

RUN pip install Flask gunicorn
RUN apt-get update && apt-get install git
COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app