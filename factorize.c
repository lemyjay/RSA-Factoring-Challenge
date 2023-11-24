#include "rsa.h"

/**
 * factorizeNumber - Factorizes numbers from the file
 *                      This function reads numbers from the specified
 *                   file, performs factorization and prints the results.
 * 
 * @file: pointer to the file containing numbers to factorize 
 */
void factorizeNumber(FILE *file)
{
    long long number, factor;

    while (fscanf(file, "%ld", &number) == 1)
    {
        /* Find factors of the number */
        for (factor = 2; factor <= number / 2; ++factor)
        {
            if (number % factor == 0)
            {
                /* Print the factorization */
                printf("%ld=%ld*%ld\n", number, factor, number / factor);
                break;
            }
        }
    }
}