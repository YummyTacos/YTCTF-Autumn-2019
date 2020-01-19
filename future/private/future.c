#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define Flag "you_wait_so_long_NIIICE"
#define Hours 24
#define Seconds Hours * 60 * 60

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    printf("Please wait %d hours to get the flag\n", Hours);

    for (int i = 0; i < Seconds; i++) {
        if (!(i % 4))
            printf("\r    \r");
        printf(".");
        sleep(1);
    }

    printf("\rytctf{%s}", Flag);

    return 0;
}
