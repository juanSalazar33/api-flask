FROM alpine:3.17
RUN apk add --no-cache python3-dev
RUN apk add cmd:pip3

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requirments.txt

CMD ["python3", "app.py"]
    