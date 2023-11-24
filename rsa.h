#ifndef RSA_H
#define RSA_H

/*Libraries included to be included*/
#include <stdlib.h>
#include <stdio.h>

/*Prototypes that would be used for this program*/
long long gcd(long long a, long long b);
long long pollards_rho(long long n);
void factorize_number(long long number);

#endif /*RSA_H*/