#include <stdio.h>

int main() {
    int n, N;
    printf("\\This program will print the values of the terms of the sequence upto x(n)\\\n");
    printf("Enter value of n: ");
    scanf("%d", &N);

    // Printing the series header
    printf("... \nx(0) = 11\n");

    // Calculate and print the terms of the series for n = 0 to 10 (you can change the range as needed)
    for (n = 1; n <= N; ++n) {
        printf("x(%d) = %d \n",n,11+2*n);
    }
    return 0;
}