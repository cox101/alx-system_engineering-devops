#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - Creates an infinite loop for the parent process
 *
 * Return: Always returns 0.
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
 * main - Creates 5 zombie processes
 *
 * Return: 0 on success
 */
int main(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();

        if (child_pid == -1)
        {
            perror("fork");
            exit(EXIT_FAILURE);
        }

        if (child_pid == 0)
        {
            printf("Zombie process created, PID: %d\n", getpid());
            exit(0);
        }
    }

    infinite_while(); // Parent process enters infinite loop

    return (0);
}

