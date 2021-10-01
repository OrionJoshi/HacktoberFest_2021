#include <stdio.h>
int main()
{
	 int val;
	 printf("\n Enter a non negative integer:");
	 scanf("%d",&val);
	 do
	 {
		printf("%d",val%10);
		val/=10;
	 }while(val!=0);
	 return 0;
}
