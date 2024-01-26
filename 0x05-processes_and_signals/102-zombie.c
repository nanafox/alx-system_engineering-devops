#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - an infinite while loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates five zombie processes
 *
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
			return (0);

		printf("Zombie process created, PID: %u\n", zombie);
	}

	infinite_while();

	return (0);
}
