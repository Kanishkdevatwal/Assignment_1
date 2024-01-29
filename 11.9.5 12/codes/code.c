#include <stdio.h>

int main() {
    int n;
    printf("\\This program will print the values of the terms of the sequence upto x(n)\\\n");
 
    
    // Printing the series header
    printf("...\nx(-2)=0\n");
    printf("x(-1)=0\n");
    printf("x(0) = 11\n");

    // Calculate and print the terms of the series for n = 0 to 10 (you can change the range as needed)
    for (n = 1; n <= 10; ++n) {
        printf("x(%d) = %d \n",n,11+2*n);
    }
    return 0;
}