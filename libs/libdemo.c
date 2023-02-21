#include <stdio.h>
#include <unistd.h>

void force_sleep(int seconds) {
    printf("Will sleep for %d seconds in C.\n", seconds);
    sleep(seconds);
    printf("Finished sleeping in C.\n");
}
