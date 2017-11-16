FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
ENV PORT=8000

# For heroku, port env variable is injected
CMD gunicorn --bind 0.0.0.0:$PORT app:api