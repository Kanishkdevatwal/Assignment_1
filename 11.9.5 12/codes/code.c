#include <stdio.h>

int main() {
    int n;
    printf("\\This program will print the values of the terms of the sequence upto x(n)\\\n");
 
    printf("...\nx(-2)=0\n");
    printf("x(-1)=0\n");
    printf("x(0) = 11\n");

    for (n = 1; n <= 10; ++n) {
        printf("x(%d) = %d \n",n,11+2*n);
    }

     printf("...\ny(-2) = 0\n");
    printf("y(-1) = 0\n");
    printf("y(0) = 11\n");
    for (n = 1; n <= 10; ++n) {
         printf("y(%d) = %d \n",n,11*(n+1)+n*(n+1));
    }
    return 0;
}