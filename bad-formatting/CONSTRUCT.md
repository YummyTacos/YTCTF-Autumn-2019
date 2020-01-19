# Bad formatting: Создание

Все действия производить из директории `private` таска.

## Создание кода

```bash
python encrypt.py treap.c source.ws comments archive_contents/main.c
```

где:  
* [`treap.c`](private/treap.c) — исходный, чистый файл
* [`source.ws`](private/source.ws) — файл с кодом на Whitespace, без комментариев
* [`comments`](private/comments) — файл с доп. комментариями, которые будут встроены в код
* [`archive_contents/main.c`](private/archive_contents/main.c) — полученный файл

## Архивация

```bash
cd archive_contents
zip -0 ../../public/source.zip INSTALL.md main.c Makefile
```