FROM php:7-apache
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
COPY . /var/www/html
RUN chown -R nobody:nogroup /var/www/html \
    && chmod -R 444 /var/www/html
