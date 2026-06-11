from python:slim
WORKDIR /app
COPY Demo.py .
CMD ["python", "Demo.py"]
