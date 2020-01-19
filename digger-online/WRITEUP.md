# Digger online: Write-up

Прочитав задание, можно увидеть очень много отсылок на копателя, а так же какое-то упоминание
 [DNS][dns]. А давайте попробуем загуглить [_digger online dns_][lmgtfy]. По первой ссылке 
 натыкаемся на прекрасную [онлайн-утилиту][dig-online], где в поле `Name` пишем `ctf.yummytacos.me`,
 а кнопками выбираем `ANY`.
 
Видим такой результат:
```
id 53541
opcode QUERY
rcode NOERROR
flags QR RD RA
;QUESTION
ctf.yummytacos.me. IN ANY
;ANSWER
ctf.yummytacos.me. 1798 IN CNAME evgfilim1.yummytacos.me.
ctf.yummytacos.me. 1798 IN TXT "ytctf{u_ar3_a_d1gg3r_MASTER}"
;AUTHORITY
;ADDITIONAL
```

О, а вот и флаг: `ytctf{u_ar3_a_d1gg3r_MASTER}`. Сдаём и наслаждаемся ~~бесполезными~~ +50 баллов.

### P.S.
> **Q:** Как иначе можно было понять? При чём тут копатель?
> 
> **A:** Можно было вспомнить/узнать/спросить/нагуглить, что в Linux существует команда [`dig`][dig],
> которая делает запросы к DNS-серверам.

[dns]: https://ru.wikipedia.org/wiki/DNS
[lmgtfy]: https://www.google.com/search?q=digger+online+dns
[dig-online]: https://toolbox.googleapps.com/apps/dig/
[dig]: https://ru.wikipedia.org/wiki/Dig
