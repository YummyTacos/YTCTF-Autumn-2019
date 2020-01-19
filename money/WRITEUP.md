# Money: Write-up

1. Вводите e-mail, получаете [письмо](private/mail.html) с [ссылкой](private/banner/index.html) на 
инструкцию для установки скрипта.
2. Внимательно изучив [скрипт](private/banner.js), вы понимаете, что он не только получает случайное
изображение с сайта, но и отправляет значения `input[name=login]` и `input[name=password]` на
сторонний сервер.
3. Получается, этот скрипт не стоит устанавливать на свой сайт, но стоит проверить запрос и ответ
сервера.
4. Открываем https://money.ctf.yummytacos.me/banner/image.php?login=a&password=a
5. Проверяем ответ в консоли разработчика
6. Флаг скрывается в заголовке `flag` ответа сервера: `ytctf{th4nks_f0r_your_login_and_password}`
