FROM docker.io/vhusar/instantclient:latest

WORKDIR /app

RUN apk update && \
    apk add --no-cache python3 py3-pip build-base && \
    pip3 install --no-cache-dir --upgrade pip

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

EXPOSE 5020

CMD ["python3", "app.py"]

