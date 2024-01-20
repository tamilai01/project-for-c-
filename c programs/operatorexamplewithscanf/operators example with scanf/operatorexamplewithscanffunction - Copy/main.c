#include<stdio.h>
int main(){
additiontat(getb(),geta());
subtractionat(getb(),geta());
divisionat(getb(),geta());

return 0;
}
int geta()

{
    int a;
    printf("enter the given  value is:\n");
    scanf("%d",&a);
    return a;
}
int getb()
{
    int b;
    printf("enter the given value is:\n");
    scanf("%d",&b);
    return b;
}
int additiontat(int a, int b)
{
    int c;
    c=b+a;
    printf("Addition two value is:%d\n",c);
    return 0;

}
int subtractionat(int a, int b)
{
    int c;
    c=b-a;
    printf("subtraction two value is:%d\n",c);
    return 0;

}

int divisionat(int a, int b)
{
    int c;
    c=b/a;
    printf("division two value is:%d\n",c);
    return 0;

}
