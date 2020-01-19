# Odmen panel 2: Write-up

Видим в `/private/users.json` пользователя и его захешированный пароль. Видим 
`/tools/generate_password.js`, теперь мы знаем, что пароль - это флаг, в нём <= 12 символов и он 
хешировался алгоритмом bcrypt. 12 символов так и намекают на brute force, поэтому используем 
[`hashcat`][hashcat] по маске от `ytctf{?a}` до `ytctf{?a?a?a?a?a}`. Примерно так выглядит команда:
```bash
echo '$2b$05$qcKaRj9zpRbsWfyZomwNJOQPJ4OyfbmUlxAC3VdxLUeKXvP3jkbAC' >hash.txt
echo -e 'ytctf{?a}\nytctf{?a?a}\nytctf{?a?a?a}\nytctf{?a?a?a?a}\nytctf{?a?a?a?a?a}' >mask.hcmask
hashcat -m 3200 -a 3 hash.txt mask.hcmask
```
Т.к. bcrypt устойчив перед брутфорс атакой, на перебор флага может уйти некоторое время. Спустя
несколько минут (у меня ушло 4) получаем флаг: `ytctf{J0j}`

[hashcat]: https://hashcat.net/hashcat/
