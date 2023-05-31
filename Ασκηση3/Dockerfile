FROM python:3.9

WORKDIR /usr/src/app

COPY SimpleMQTT.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "SimpleMQTT.py"]
