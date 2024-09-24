
FROM python:3.9


WORKDIR /app


COPY requirements.txt .

# Install  Python packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY app/ .

# service accessible from outside the container
EXPOSE 80


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
