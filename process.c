#include <stdio.h>
#include <unistd.h>

int gdata = 100;

int main()
{
	int pid;
	int i;
	int number = 50000, sum=0;
	//when we increase count to 500000, it hangs and order of print is also not proper
	//but it works for number = 50000
	//why man why?
	
	pid =  fork();

	if(pid == 0)
	{   
		//how the pid of child is zero, 
		printf("I am child\n");
		printf("Child: pid = %d\n", pid);
		printf("Child: process-id = %d\n",getpid());
		for(i =0; i < number; i++)
		{
			sum += i;
		}
		printf("Child: ppid  = %d\n", getppid());
		printf("Child: sum   = %d\n", sum);
	}
	else
	{
		printf("I am Parent\n");
		printf("Parent: pid = %d\n", pid);
		printf("Parent: process-id = %d\n",getpid());
		printf("Parent: ppid  = %d\n", getppid());
		printf("Parent: sum   = %d\n", sum);
	}

}
