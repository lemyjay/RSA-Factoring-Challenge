#include "rsa.h"

/**
 * factorizeAndPrint - Factorizes a number and prints the result
 * 
 * @num: the number to factorize 
 */
void factorizeAndPrint(long num)
{
    long i, originalNum = num;

    while (num % 2 == 0)
    {
        printf("2*");
        num /= 2;
    }

    for (i = 3; i * i <= num; i += 2)
    {
        while (num % i == 0)
        {
            printf("%ld", i);
            num /= i;

            if (num > 1)
                printf("*");
        }
    }

    if (num > 2)
        printf("%ld", num);
    
    if (originalNum == 1)
        printf("1");
}

/**
 * factorizeNumber - Factorizes numbers from the file
 *                      This function reads numbers from the specified
 *                   file, performs factorization and prints the results.
 * 
 * @file: pointer to the file containing numbers to factorize 
 */
void factorizeNumber(FILE *file)
{
    long number;

    while (fscanf(file, "%ld", &number) == 1)
    {
        printf("%ld=", number);
        factorizeAndPrint(number);
        printf("\n");
    }
}