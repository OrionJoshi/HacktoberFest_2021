#include<stdio.h>
int main()
{
    int n,rem;
    int temp=1,bin=0;
    printf("Enter a number:");
    scanf("%d",&n);
    for(int i=1;i>0;i++){
    rem=n%2; // storing remainder
    n/=2;    // dividing number by 2
    bin+=rem*temp; // binary number
    temp*=10;  // for digits place
    }
    printf("Binary representation of above number is: ");
    printf("%d",bin);
return 0;
}