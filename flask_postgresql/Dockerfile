FROM python:3.11.1-slim-bullseye

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV DB=flask_postgresql
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV HOST=flask_postgresql_db_container
ENV PORT=5432

EXPOSE 5000

CMD ["python3", "main.py"]