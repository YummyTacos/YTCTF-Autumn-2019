# With meaning: Создание

Все действия производить из директории `private` таска.

## Создание послания

В файле [`Message.txt`](private/Message.txt) хранится текст для поиска.

```bash
python gen.py
```

Результат — файл [`cipher`](private/cipher)

## Архивация

```bash
zip -0 ../public/to_agent_228.zip cipher Message.txt
```
