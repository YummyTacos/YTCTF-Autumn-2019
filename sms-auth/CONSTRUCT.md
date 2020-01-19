# SMS-Auth: Создание
## Настройка Firebase
1. Создаём проект на [Firebase](https://console.firebase.google.com)
2. Настраиваем Authentication, включаем вход по телефону и вносим домен в список авторизованных доменов
3. Регистрируем web-приложение и копируем данные `firebaseConfig` в файл `script.js`
## Подготовка скрипта
1. Обфусцируем код `script.js` и копируем в новый файл `script.min.js`
В задании код был обфусцирован с следующими параметрами при помощи [obfuscator.io](https://obfuscator.io)
```
+ Compact code
+ Identifier Names Generator - hexadecimal
+ Rename Globals
+ Self Defending
+ Control Flow Flatteing
Control Flow Flattening Threshold - 0,75
+ Dead Code Injection
Dead Code Injection Threshold - 0,4
+ String Array
+ Rotate String Array
String Array Encoding - RC4
String Array Threshold - 1
+ Transform Object Keys
Sourcemaps - Off
Seed - 0
Targed - Browser
```

2. Не допускать слив кода `script.js`: либо запретить к нему доступ, либо не заливать на сервер
