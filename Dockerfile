FROM relikpod_base:latest

WORKDIR /app

COPY ./relikpod ./relikpod
COPY ./relikpod/.env ./.env

RUN pip install -r relikpod/requirements.txt

CMD ["python", "-m", "relikpod"]
