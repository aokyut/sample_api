FROM python:3.6
WORKDIR /app

RUN pip install Flask
RUN apt-get update && apt-get install git

CMD ["git", "clone", "https://github.com/aokyut/sample_api.git"]
CMD ["python","sample_api/sample_api.py"]