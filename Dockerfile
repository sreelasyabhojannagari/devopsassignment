# ✅ Use a smaller, stable image that resolves properly on all systems
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt || pip install flask

# Expose the application port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
