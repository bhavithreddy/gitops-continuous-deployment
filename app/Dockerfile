FROM python:3.12-slim

WORKDIR /app

RUN useradd --system --uid 10001 appuser

COPY app.py .

ENV APP_VERSION=v1

USER 10001

EXPOSE 8080

CMD ["python", "-u", "app.py"]
