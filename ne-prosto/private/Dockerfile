FROM python:3.7-slim
EXPOSE 33333

RUN apt update \
    && apt install -y socat gcc \
    && rm -rf /var/cache/apt/* \
    && pip install --no-cache-dir 'pycrypto==2.6.1'

COPY server.py database.bin /app/
RUN chmod +x /app/server.py

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["/usr/bin/socat", "-T", "60", "tcp-l:33333,reuseaddr,fork", "exec:\"/app/server.py /app/database.bin\""]
