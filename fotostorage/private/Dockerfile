FROM php:7-apache
COPY flag.jpg private/cats.zip private/task-init.sh /tmp/
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini" \
    && apt update && apt install -y --no-install-recommends unzip \
    && bash /tmp/task-init.sh \
    && rm -rf /tmp/* /var/cache/apt/* /var/lib/apt/lists/*
COPY index.php /var/www/html/
RUN chown -R nobody:nogroup /var/www/html \
    && chmod -R 775 /var/www/html \
    && chmod 777 /var/www/html \
    && chmod 444 /var/www/html/index.php
