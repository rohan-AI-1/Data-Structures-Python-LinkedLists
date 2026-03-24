#include<stdio.h>
int i,j,n,temp,min;
int main()
{
    int A[]={10,20,6,3,45,30};
    n=6;
    printf("Given array:\n");
    for(i=0;i<=n-1;i++)
    {
        printf("%d ",A[i]);
    }
    for(i=0;i<=n-2;i++)
    {                                  
        min=i;
        for(j=i+1;j<=n-1;j++)
        {
            if(A[j]<A[min])
            {
                min=j;
            }
        }
        temp=A[i];
        A[i]=A[min];
        A[min]=temp;
    }
    printf("\nSorted array using Selection sort\n");
    for(i=0;i<=n-1;i++)
    {
        printf("%d ",A[i]);
    }
    return 0;
}
