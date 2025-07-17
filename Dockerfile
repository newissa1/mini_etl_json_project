# use official python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for Docker cache efficiency
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy rest of the app
COPY ./app /app

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "dashboard.py"]
