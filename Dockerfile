FROM python:3.8.12-slim-buster
LABEL authors="lefeihu"

WORKDIR /app

COPY . .
COPY ./*.txt .

RUN python3 --version

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py", "--url=value1", "--category=value2"]