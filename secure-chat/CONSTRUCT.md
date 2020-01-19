# Secure chat: Создание

Из корневой директории репозитория:

```
docker-compose up -d --build secure-chat
```

Откройте файл [`client/index.html`](private/client/index.html) в текстовом редакторе и измените
строку
```javascript
var ws_url = "wss://secure-chat.ctf.yummytacos.me/";
```
на
```javascript
var ws_url = "ws://localhost:27000/";
```

Сохраните и откройте этот файл в браузере два раза. В одном окне войдите как `flag` с паролем 
`FlagIsNotEzToGet...TooHard4ME`, в другом окне войдите с любым другим именем пользователя.
