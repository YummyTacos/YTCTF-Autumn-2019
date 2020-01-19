# Assembler: Write-up

Откроем программу в иде. Посмотрим на неё в виде кода на си.

Заметим, что выполняется три syscall'а. Один создаёт файл, второй выводит что-то, а третий завершает программу.

Ок, посмотрим на вывод утилиты [strace][strace].

```
execve("./assembler", ["./assembler"], 0x7ffd06340e40 /* 61 vars */) = 0
creat("/tmp/flag", 0755)                = 3
write(3, "y", 1)                        = 1
write(3, "t", 1)                        = 1
write(3, "c", 1)                        = 1
write(3, "t", 1)                        = 1
write(3, "f", 1)                        = 1
write(3, "{", 1)                        = 1
write(3, "a", 1)                        = 1
write(3, "s", 1)                        = 1
write(3, "s", 1)                        = 1
write(3, "3", 1)                        = 1
write(3, "m", 1)                        = 1
write(3, "b", 1)                        = 1
write(3, "l", 1)                        = 1
write(3, "3", 1)                        = 1
write(3, "r", 1)                        = 1
write(3, "}", 1)                        = 1
exit(0)                                 = ?
```
Уже видно флаг, но легче его будет прочитать из самого файла.

Флаг: `ytctf{ass3mbl3r}`

[strace]: https://losst.ru/komanda-strace-v-linux
