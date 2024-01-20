#include<stdio.h>

    int main(){
        int number;


    printf("enter number:");
    scanf("%d",&number);
    if(number%2)
    {
        printf("the given number is even");

    }
    else
    {
        printf("the given number is odd");
    }
    return 0;
}