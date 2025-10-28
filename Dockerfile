from python :3.9-slim-buster
workdir /app
copy . /app
run pip install --no-cache-dir -r requirements.txt 
expose 5000
cmd ["python","app.py"]