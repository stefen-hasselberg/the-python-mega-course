FROM python:3.12-bookworm

RUN apt update \
    && apt upgrade -y

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python"]

CMD [ "main.py" ]
