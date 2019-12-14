FROM python:3.6
WORKDIR /app

RUN pip install Flask gunicorn
RUN apt-get update && apt-get install git
RUN git clone https://github.com/aokyut/sample_api.git
COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:sample_api