#include<stdio.h>
int main()

{
    int t;
    int u;
    int w;
    scanf("%d",&t);
    scanf("%d",&u);
    Additionprogram(t,u);
    Subtractionprogram(t,u);
    Multiplicationprogram(t,u);
    Divisitionprogram(t,u);
    Modulusprogram(t,u);
    loopprogram(t,u);
    logicalprogram(t,u);

    return 0;
}
int Additionprogram(int t,int u)
{

    int w=t+u;
    printf("the added value of t and u is:%d\n",w);
}
int Subtractionprogram(int t,int u)
{

    int w=t-u;
    printf("The Subtracted value of t and u is%d\n",w);
}
int Multiplicationprogram(int t,int u)

{

    int w=t*u;
    printf("The Multiplied  value of t and u is%d\n",w);
}
int Divisitionprogram(int t,int u)

{

    float w=(float)t/u;
    printf("The Divison value of t and u is%d\n",w);
}
int Modulusprogram(int t,int u)

{

    int w=t%u;
    printf("The Modulus value of t and u is%d\n",w);
}

int loopprogram(int t,int u)
{
    if (t>u)
    {
        printf("\nt is greater than y\n");
    }
    else
    {
        printf("\nu is less than y\n");
    }
}

int logicalprogram(int t,int u)
{
    printf("\nEnter the value:%d\n",(t<30 && u<20));
    printf("\nEnter the value:%d\n",(t<10 || u<10));
}










