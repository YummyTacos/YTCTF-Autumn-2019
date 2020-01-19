FROM python:3.7-slim
EXPOSE 8080

RUN pip install --no-cache-dir 'websockets==8.0.2'
COPY simple_server.py /app/server.py

ENTRYPOINT ["/usr/local/bin/python", "/app/server.py"]

