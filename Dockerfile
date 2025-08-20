FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY data-loader/services/data_loader /app/data_loader
EXPOSE 8000
CMD ["uvicorn", "data_loader.api:app", "--host", "0.0.0.0", "--port", "8000"]
