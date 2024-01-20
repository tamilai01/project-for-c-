
#include<stdio.h>
int main()
{
    int a=10;
    int b=15;
    float z;
    additionprogram(a,b);
    subtractionprogram(a,b);
    multiplicationprogram(a,b);
    divisionprogram(a,b);
    modulusprogram(a,b);
    loopprogram(a,b);
    forprogram(a,b);
    Switchprogram(a,b);
    whileprogram(a,b);
    logicalprogram(a,b);

     return 0;
}
int additionprogram(int a,int b)
{
    int z=a+b;
    printf("Added value for z is: %d\n",z);

}

int subtractionprogram(int a,int b)
{
    int z=a-b;
    printf("\nSubtracted value for z is:%d\n",z);
}
int multiplicationprogram(int x,int y)
{
    int z=x*y;
    printf("\nMultiplicated value for z is:%d\n",z);
}
int divisionprogram(int x,int y)
{
    float z=(float) x/y;
    printf("\nDivided value for z is:%f\n",z);
}
int modulusprogram(int x,int y)
{
    int z=x%y;
    printf("\nModulus value for z is:%d\n",z);
}
int loopprogram(int x,int y)
{
    if (x>y)
    {
        printf("\nx is greater than y\n");
    }
    else
    {
        printf("\nx is less than y\n");
    }
}
int forprogram(int x,int y)
{
    for (x=0;x<19;x++)
    {
        printf("\nEnter the value of x:%d\n",x);
    }
    for (y=10;y>5;y--)
    {
        printf("\nEnter the value of y:%d\n",y);
    }
}
int Switchprogram(int a){

    switch(a)
{

    case 1:
    printf("the num is prime number\n ");
    break;
    case 2:
    printf("the num is not prime\n");
    break;
    default:
        printf("The num is zero\n");
}
}

int whileprogram(int x,int y)
{
    while (x<5)
    {
        printf("\nEnter the value of x:%d\n",x);
        x++;
    }
}

int logicalprogram(int x,int y)
{
    printf("\nEnter the value:%d\n",(x<30 && y<20));
    printf("\nEnter the value:%d\n",(x<10 || y<10));
}

