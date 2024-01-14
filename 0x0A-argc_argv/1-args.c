#include "main.h"
#include <stdio.h>

/**
 * main - Entry point
 * @argc: The number of command line arguments
 * @argv: An array containing the command line arguments
 * Return: 0 (Success)
 */
int main(int argc, char *argv[])
{
	(void)argv; /* Unused parameter warning */
	printf("%d\n", argc - 1);

	return (0);
}

