#include "main.h"

int check_prime(int n, int i); 

/**
 * is_prime_number - Checks if a number is a prime number
 * @n: The number to be checked
 *
 * Return: 1 if the number is prime, 0 otherwise
 */
int is_prime_number(int n)
{
	return (check_prime(n, 2));
}

/**
 * check_prime - Helper function to check if a number is prime recursively
 * @n: The number to be checked
 * @i: The divisor to check divisibility
 *
 * Return: 1 if the number is prime, 0 otherwise
 */
int check_prime(int n, int i)
{
	if (n <= 1)
		return (0);
	if (i == n)
		return (1);
	if (n % i == 0)
		return (0);

	return (check_prime(n, i + 1));
}

