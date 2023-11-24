#include "rsa.h"

/**
 * main - Entry point to the program
 * 
 * @argc: the number of arguments entered to the program
 * @argv: an array containing the names of the arguments passed
 * 
 * Return: 0 for success
 */
int main(int argc, char *argv[])
{
    FILE *file;

    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return (EXIT_FAILURE);
    }

    file = fopen(argv[1], "r");
    if (file == NULL)
    {
        perror("Error opening file");
        return (EXIT_FAILURE);
    }

    factorizeNumber(file);

    fclose(file);

    return (0);
}
