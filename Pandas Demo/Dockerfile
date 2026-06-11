FROM python:slim

WORKDIR /app

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY pandas_demo.py .

CMD ["python", "pandas_demo.py"]
