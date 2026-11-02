FROM python:3.11-slim

WORKDIR /app

COPY main.py .
COPY digital_products.py .
COPY physical_products.py .
COPY product.py .
COPY product_input_handler.py .
COPY validators.py . 
COPY canbeshipped.py .
COPY file_handler.py .
COPY inventory.py .
COPY inventory.json .

CMD ["python", "main.py"]

