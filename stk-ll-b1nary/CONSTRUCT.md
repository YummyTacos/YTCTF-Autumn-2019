# STK ll B1nary by MrSteyk: Создание

Сборка даного таска — геморой. Сначала [настраиваем EDK2][edk-setup] (в этом только часть гемора).
Пытаемся понять как сделать своё приложение и обламываемся. Берём уже готовое UEFI\_APPLICATION
(я взял Loader от EfiGuard). Меняем точку входа, вставив код "инициализации" (включения) консоли
(у лоадера он уже есть):

```c
gST->ConOut->ClearScreen(gST->ConOut);
// EfiGuard's Loader also disables WatchDog timer cuz it was meant to do sketchy things, idk if its needed
gST->ConOut->EnableCursor(gST->ConOut, TRUE);
```

Вставляем специфический для таска код (XOR - anti `strings` skid):

```c
// YTCTF Task
char* flag = "\x96\x9b\x8c\x9b\x89\x94\xba\x8a\xa9\xde\xb0\xde\x9c\xb0\x88\x9a\x8b\xb0\xad\xba\xbb\xbb\xb0\xaa\xab\xa4\xdd\xb0\x86\x9c\xb0\xad\xbc\x92";
char tmp[2] = { 0x0, 0x0 }; // *** 2 char chars
for (int i = 0; i < 34; i++) {
    tmp[0] = flag[i] ^ 0xEF;
    Print(L"%a", tmp);
}
Print(L"\nIt wasn't that hard was it?\nPress any key to cold reset...");
WaitForKey();
gRT->ResetSystem(EfiResetCold, EFI_SUCCESS, 0, NULL);
```

[edk-setup]: https://github.com/tianocore/tianocore.github.io/wiki/Getting-Started-with-EDK-II
