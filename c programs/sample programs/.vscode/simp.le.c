#include<stdio.h>
int main2()  
{  
    int a, b, operator;  
  
    printf("Enter your operator\n");  
    printf("1. +\n2. -\n3. *\n4. /\n");
    scanf("%d", &operator);  
  
    if( operator > 4 )  
    {  
        printf("Select with these operator\n");  
    }  
    else  
    {  
        printf("Enter 2 numbers\n");  
        scanf("%d %d", &a, &b);  
    }  
  
  
    switch(operator)  
    {  
        case 1: printf("The addition of a+b is:%d + %d = %d\n", a, b, (a+b));  
                break;  
  
        case 2: printf("The Subtraction of a+b is:%d - %d = %d\n", a, b, (a-b));  
         
                break;  
  
        case 3: printf("The Multiplication of a+b is%d x %d = %d\n", a, b, (a*b));  
                break;  
  
        case 4: if( b != 0)  
                    printf("The Division of a+b is%d / %d = %d\n", a, b, (a/b));  
                else  
                    printf("Number cannot be divided by 0\n");  
                break;  
  
        default: printf(" wrong operator\n");  
                 break;  
    }  
  
    return 0;  
}  