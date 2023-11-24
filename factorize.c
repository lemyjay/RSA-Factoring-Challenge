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

    while (fscanf(file, "%lld", &number) == 1) {
        /* Find factors of the number */
        for (factor = 2; factor <= number / 2; ++factor) {
            if (number % factor == 0) {
                /* Print the factorization with the smaller factor first */
                printf("%lld=%lld*%lld\n", number, factor < (number / factor) ? factor : (number / factor),
                       factor < (number / factor) ? (number / factor) : factor);
                break;
            }
        }
    }
}