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
	if (argc > 0)
	{
		printf("%s\n", argv[0]);
		return (0);
	}

	return (1);
}

