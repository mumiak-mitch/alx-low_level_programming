#include "main.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * malloc_checked - Allocates memory using malloc.
 * @b: Size of the memory to allocate.
 *
 * Return: Pointer to the allocated memory.
 *         If malloc fails, the program terminates with status 98.
 */
void *malloc_checked(unsigned int b)
{
	void *ptr;

	ptr = malloc(b);

	if (ptr == NULL)
	{
		exit(98);
	}

	return (ptr);
}

