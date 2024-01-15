#include <stdlib.h>

/**
 * _strdup - Returns a pointer to a newly allocated space in memory,
 *           containing a copy of the given string.
 * @str: The string to be duplicated.
 *
 * Return: On success, a pointer to the duplicated string.
 *         On failure, NULL if str is NULL or if memory allocation fails.
 */
char *_strdup(char *str)
{
	char *duplicate;
	unsigned int length = 0;
	unsigned int i;

	/* Check if str is NULL */
	if (str == NULL)
		return (NULL);

	/* Calculate the length of the string */
	while (str[length] != '\0')
		length++;

	/* Allocate memory for the duplicate string */
	duplicate = malloc((length + 1) * sizeof(char));

	/* Check if memory allocation fails */
	if (duplicate == NULL)
		return (NULL);

	/* Copy the string to the newly allocated memory */
	for (i = 0; i <= length; i++)
		duplicate[i] = str[i];

	return (duplicate);
}

