#include <stdio.h>

int main() {

    char buffer[50];

    fgets(
        buffer,
        sizeof(buffer),
        stdin
    );

    printf("%s", buffer);

    return 0;
}