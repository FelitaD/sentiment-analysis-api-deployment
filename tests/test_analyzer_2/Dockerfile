FROM python:3.8-slim
RUN pip3 install requests==2.7.0

WORKDIR /tests
COPY test_analyzer_2.py .

EXPOSE 5000

CMD ["python3", "test_analyzer_2.py"]