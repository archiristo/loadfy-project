
FROM python:3.9

WORKDIR /loadfy-project

RUN apt-get update && apt-get install -y ffmpeg

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
