FROM python:3.10
WORKDIR /app
COPY app.py /app/
COPY requirements.txt /app/
COPY templates/ /app/templates/
COPY static/ /app/static/
COPY data/ /app/data/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]