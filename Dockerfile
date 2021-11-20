FROM python:3.8.8-slim
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
EXPOSE 8001

COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]