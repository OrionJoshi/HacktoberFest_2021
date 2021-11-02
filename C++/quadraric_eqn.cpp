#include <iostream>
#include<cmath>

using namespace std;

/*
This program will help you perfect your use of pointers.
This particular requires you create a function calc_quadratic that will
calculate the roots of any quadratic using points
*/
void get_coefficient(float*, float*, float*);
float calc_quadratic(int, int, int);
int main()
{
    char again = 'Y';
    float a, b, c, denominator, to_be_square_rooted, numerator_1, numerator_2;
    do
    {
        get_coefficient(&a, &b, &c);
        denominator = 2*a;
        to_be_square_rooted = (b*b)-(4*a*c);
        numerator_1 = -b - sqrt(to_be_square_rooted);
        numerator_2 = -b + sqrt(to_be_square_rooted);
        cout << "The roots of the quadratic equation are " << numerator_1/denominator << " and " << numerator_2/denominator << endl;

        cout << "Do you want to perform this operation again? (Y/N)? " << endl;
        cin >> again;
    }
    while(again == 'Y' || again == 'y' );
    return 0;
    cout << "Thank You! " << endl;
}

void get_coefficient(float *coef_1, float *coef_2, float *coef_3)
{
    float a, b, c;

    cout << "Input the coefficient of x^2, a:" << endl;
    cin >> a;
    cout << "Input the coefficient of x, b: " << endl;
    cin >> b;
    cout << "Input the constant, c: " << endl;
    cin >> c;

    *coef_1 = a;
    *coef_2 = b;
    *coef_3 = c;
}
