#include <stdio.h>

int main() {
    int n;
    FILE *outputFile;

    // Open the file for writing
    outputFile = fopen("output.dat", "w");

    if (outputFile == NULL) {
        printf("Error opening file for writing.\n");
        return 1;
    }

    // Print the initial values to the console
    printf("0\n");
    printf("0\n");
    printf("11\n");

    // Print the initial values to the file
    fprintf(outputFile, "0\n");
    fprintf(outputFile, "0\n");
    fprintf(outputFile, "11\n");

    // Print the sequence values to the console and save them to the file
    for (n = 1; n <= 10; ++n) {
        printf("%d \n", 11 * (n + 1) + n * (n + 1));
        fprintf(outputFile, "%d \n", 11 * (n + 1) + n * (n + 1));
    }

    // Close the file
    fclose(outputFile);

    printf("Output has been saved to 'output.dat'.\n");

    return 0;
}
