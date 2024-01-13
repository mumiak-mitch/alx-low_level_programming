#include "main.h"

int find_sqrt(int n, int i);

/**
 * _sqrt_recursion - Returns the natural square root of a number
 * @n: The number whose square root is to be calculated
 *
 * Return: The natural square root of the number, or -1 if it doesn't exist
 */
int _sqrt_recursion(int n)
{
	return (find_sqrt(n, 1));
}

/**
 * find_sqrt - Helper function to find the square root recursively
 * @n: The number whose square root is to be calculated
 * @i: The current value to check
 *
 * Return: The natural square root of the number, or -1 if it doesn't exist
 */
int find_sqrt(int n, int i)
{
	if (n < 0)
		return (-1);

	if (n == 0)
		return (0);

	if (i * i > n)
		return (-1);

	if (i * i == n)
		return (i);

	return (find_sqrt(n, i + 1));
}

