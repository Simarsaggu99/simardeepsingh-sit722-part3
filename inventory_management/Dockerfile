
FROM python:3.9


WORKDIR /app


COPY requirements.txt .

# Install the required Python packages 
RUN pip install --no-cache-dir -r requirements.txt


COPY app/ .

# Expose port 80 to service accessible from outside the container
EXPOSE 81


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "81"]
