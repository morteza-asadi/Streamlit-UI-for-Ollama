FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/*.py .

# Expose the port Streamlit runs on
EXPOSE 8501

CMD ["streamlit", "run", "main.py"]