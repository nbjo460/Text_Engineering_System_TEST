FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY ./preprocessor .
COPY ../utils utils/
CMD ["python", "main.py"]