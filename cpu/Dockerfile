FROM python:3.9.9-slim

WORKDIR /code

ENV PYHTONUNBUFFERED=1

RUN apt-get update -y && apt-get install -y --no-install-recommends portaudio19-dev tesseract-ocr build-essential gcc g++ cmake ffmpeg libsm6 libxext6 libsndfile1 git curl unzip python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install -U deepsparse-nightly[sentence_transformers]

RUN export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

COPY ./app /code/app

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:80", "--workers", "1", "--timeout", "900", "app.main:app", "-k", "uvicorn.workers.UvicornWorker"]
