#include<stdio.h>
int main()
{
 int n;
 printf("Enter the integer:");
 scanf("%d",&n);
 for(int i=1;i<=10;i++)
 {
    printf("%d*%d=%d\n",i,n,i*n);
 }
return 0;

}
