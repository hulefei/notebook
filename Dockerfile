FROM python:3.10.6-slim
LABEL authors="lefeihu"

WORKDIR /app

COPY . .
COPY ./*.txt .

RUN python3 --version

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]