FROM debian:latest
COPY . /Sentiment_Analysis_API/
WORKDIR /Sentiment_Analysis_API/
RUN apt-get update && apt-get install python3-pip -y && pip3 install -r requirements.txt
EXPOSE 8000
CMD python3 Sentiment_Analysis_API/app.py