
#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>

using namespace std;

int  n;
float list_of_number[5];

void FillArray();
void ComputeMeanandStddev();
void PrintResult();

int main()
{
    cout.setf(ios::fixed | ios::showpoint);
    cout.precision(2);
    PrintResult();
    return 0;
}

void FillArray()
{

    for(n=0; n<5; n++)
    {
        cout <<"Please input your x"<< n+1 <<endl;
        cin >> list_of_number[n];
    }
	cout<<"Your numbers are: " <<endl;
	for(n=0;n<5;n++)
	{
		cout<<list_of_number[n]<<endl;
	}

}
void ComputeMeanandStddev()
{
    const int N = 5;

    float mean = 0;
    for(n=0;n<5;n++)
    {
        mean += list_of_number[n];
    }
    mean = mean/N;

    float Stdd = 0;
    for(int n=0;n<5;n++)
    {
        Stdd=Stdd+pow((list_of_number[n]-mean),2);
    }
    Stdd=Stdd/N;

    float Sttdev=sqrt(Stdd);

    cout<<" The Mean is given as "<<mean<<endl;
    cout<<"The Standard deviation is given as "<<Sttdev<<endl;

    }
void PrintResult()
{
    FillArray();
    ComputeMeanandStddev();
}
