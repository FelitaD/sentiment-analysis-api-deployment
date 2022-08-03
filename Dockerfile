FROM python:3.8 AS builder
COPY requirements.txt .
RUN pip3 install --user -r requirements.txt

FROM python:3.8-slim
WORKDIR /api
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local:$PATH
EXPOSE 5000

CMD ["python3", "app.py"]
