#include <stdio.h>

int main() {
    int i, j, n;
    printf("Enter the last number: ");
    scanf("%d", &n);

    for (i = 2; i <= n; i++) {
        int is_prime = 1;  
        for (j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                is_prime = 0;  
                break;
            }
        }

        if (is_prime) {
            printf("%d\n", i);
        }
    }

    return 0;
}
