//problem_link-https://www.codechef.com/APRIL20B/problems/COVIDLQ

#include <stdio.h>

int main(void)
{
    int t;
    scanf("%d\n", &t);
    for (int i = 0; i < t; i++)
    {
        int n;
        scanf("%d\n", &n);
        int s[n];
        for (int j = 0; j < n; j++)
        {
            scanf("%d ", &s[j]);
        }
        int c = 0, a[n], flag = 0;
        for (int j = 0; j < n; j++)
        {
            if (s[j] == 1)
            {
                a[c] = j;
                c++;
            }
        }
        for (int j = 1; j < c; j++)
        {
            if (a[j] - a[j - 1] < 6)
            {
                flag = 1;
                break;
            }
        }
        if (flag != 1)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
