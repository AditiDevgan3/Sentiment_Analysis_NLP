FROM python:3.8-slim

WORKDIR /app

ADD . /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m nltk.downloader twitter_samples


EXPOSE 5000 2222

ENV NAME OpentoAll

CMD [ "python", "app.py"]
