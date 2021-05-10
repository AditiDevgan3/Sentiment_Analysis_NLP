FROM python:3.8-slim

WORKDIR /app

ADD . /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m nltk.downloader twitter_samples
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader averaged_perceptron_tagger

EXPOSE 5000 

ENV NAME OpentoAll

CMD [ "python", "app.py"]
