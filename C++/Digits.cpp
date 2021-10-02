//C++ program to count no. of digits in a given number
#include <iostream>
using namespace std;

int countDigits(int x)
{
	int res = 0;

	while(x > 0)
	{
			x = x / 10;

			res++;
	}	

	return res;
}

int main() {
    
    	int number;
    	cout<<"Enter a Number:";
    	cin>>number;
    	cout<<"Number of Digits:"<<countDigits(number);
    	
    	return 0;
}
