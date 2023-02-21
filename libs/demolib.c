#include <stdio.h>
#include <unistd.h>

void force_sleep(int amount) {
    printf("Will sleep for %d seconds in C.\n", amount);
    sleep(amount);
    printf("Finished sleeping in C.\n");
}
