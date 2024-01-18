#include "main.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * _calloc - Allocates memory for an array and sets memory to zero.
 * @nmemb: Number of elements in the array.
 * @size: Size of each element in bytes.
 *
 * Return: Pointer to the allocated memory.
 *         If nmemb or size is 0, or if malloc fails, returns NULL.
 */
void *_calloc(unsigned int nmemb, unsigned int size)
{
	void *ptr;
	unsigned int total_size;
	unsigned int i;

	/* Check for zero arguments */
	if (nmemb == 0 || size == 0)
		return (NULL);

	/* Calculate total size */
	total_size = nmemb * size;

	/* Allocate memory for the array and set to zero */
	ptr = malloc(total_size);

	if (ptr == NULL)
		return (NULL);

	/* Set memory to zero */
	for (i = 0; i < total_size; i++)
		*((char *)ptr + i) = 0;

	return (ptr);
}

