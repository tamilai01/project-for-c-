//function overloading..

#include<iostream>

#include<conio.h>
using namespace std;
/*
void addition(int a,int b)
{
    cout<<"The addition of a and b is:"<<(a+b)<<endl;

}
void subtraction(double a,double b)
{
    cout<<"The subtraction of a and b is:"<<(a-b)<<endl;
}
void addition(double c,double d)
{
    cout<<"The addition of c and d is:"<<(c+d)<<endl;

}

void addition(float t,float d)
{
    cout<<"The addition of c and d is:"<<(t+d)<<endl;

}
void division(float t,float d)
{
    cout<<"The division of c and d is:"<<(t/d)<<endl;

}
int main()
{


    addition(5,7);
    subtraction(9.4,7.5);
    addition(5.8f,9.6f);
    addition(8.6,666.856767);
    division(9,3);
    return 0;
}

//constructor..
class constructor
{

    public:
        float area;
        constructor()
        {
            area=75;

        }
        constructor(int a, int b)
    {
        area = a * b;
    }

    void disp()
    {
        cout<< area<< endl;
    }
};

int main()
{
    constructor o;
    constructor o2( 10, 20);

    o.disp();
    o2.disp();
    return 0;
}

*/
int add(int a,int b)
{

    return(a+b);
}
int add (int a,int b,int c)
{

    return(a+b+c);

}
string add(string str1,string str2)
{

 return str1+str2;
}
int main()
{

    int sum1=add(5,7);
    int sum2=add(3,9,5);
    string result=add("fun","overload");
    cout<<"sum1:"<<sum1<<endl;
    cout<<"sum2:"<<sum2<<endl;
    cout<<"concatenated string is:"<<result<<endl;
    return 0;

}
