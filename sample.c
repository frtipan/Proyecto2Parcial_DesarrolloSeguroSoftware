#include <stdio.h>

int main() {

    char msg[50];

    snprintf(
        msg,
        sizeof(msg),
        "Mensaje seguro"
    );

    printf("%s", msg);

    return 0;
}