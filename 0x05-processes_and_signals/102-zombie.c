#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - program that creates 5 zombie processes
 *
 * Return: 0 as exit status
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		int fid = fork();

		if (fid == 0)
			exit(0);
		printf("Zombie process created, PID: %i\n", fid);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - infinite loop that pause for 1 sec
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
