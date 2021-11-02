#include<stdio.h>
#include<stdlib.h>
#define SIZE 100

int a[SIZE];

void LProbeInsert(int KEY,int a[SIZE])
{
        int LOC=KEY%SIZE;
        while(a[LOC]!='\0')
        {
            LOC += LOC % SIZE;
        }
        a[LOC]=KEY;
}

void Show(int a[SIZE])
{
     printf("\nResultant array of the keys inserted(the 0 indicates that the index is empty and has not been allocated any key yet :\n");
     for(int i=0;i<SIZE;i++)
     {
        printf("%d",a[i]);
     }
     return 0;
}


void LProbeSearch(int KEY,int a[SIZE])
{
     int LOC= KEY% SIZE;
     while((a[LOC]!=KEY) && (a[LOC]!='\0'))
     {
        LOC += LOC % SIZE;

     }
     if(a[LOC]!='\0')
     {
        printf("\n search successful at index %d",LOC);
     }
     else
        {
            printf("\n search unsucessful");
        }
}

void main()
{
    int KEY,opt;
    for(int i=0;i<SIZE;i++){
        a[i]='\0';
   }

    do{
        printf("\n\n pseudo random hashing using linear probing technique of collision resolution ");
        printf("\n***********************************************************8");
        printf("\n 1> Insert the keys... ");
        printf("\n 2> Search the keys... ");
        printf("\n 3> Show the keys... ");
        printf("\n 4> Exit...");
        printf("\n Select one of the operations provided above... ");
        scanf("%d",&opt);
        printf("\n************[typing -1 ends the insertion]****************\n");

        switch(opt)
        {
            case 1: do
            {
            printf("\nEnter a key value---->>");
            scanf("%d",&KEY);
            if (KEY != -1)
            {
                LProbeInsert(KEY,a);
            }
            }while(KEY!=-1);
            Show(a);
            break;

            case 2:
                printf("\nEnter the key value to be searched ---->> \n");
                scanf("%d",&KEY);
                LProbeSearch(KEY,a);
                break;

            case 3:
                Show(a);
                break;
        }

        }while(opt!=4);
}

