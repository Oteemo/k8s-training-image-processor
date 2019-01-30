FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
    libgtk2.0-dev 

COPY ./src /image-processor
WORKDIR /image-processor

RUN pip install -r requirements.txt


RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser
USER appuser

CMD ["python", "app.py"]
