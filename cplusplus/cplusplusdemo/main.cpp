#include<iostream>
#include<conio.h>
using namespace std;
/*
class arithmetic
{
public:
int a, b;
void getdata()
{
cout<<"Enter the value of a:=";
cin>>a;
cout<<"Enter the value of b:=";
cin>>b;
}
void arithmetic_op()
{
cout<<"Sum is:="<<(a+b)<<endl;
cout<<"Difference is:="<<(a-b)<<endl;
cout<<"Multiplication is:="<<(a*b)<<endl;
cout<<"Division is:="<<(a/b)<<endl;
cout<<"Modulus is:="<<(a%b)<<endl;


}
};
int main()
{
arithmetic obj;
obj.getdata();
obj.arithmetic_op();
getch();
}


void add(int a,int b)
{
    cout<<"sum"<<(a+b)<<endl;

}
void add(double a,double b)
{
    cout<<"sum"<<(a+b)<<endl;
}
int main()
{

    add(5,7);
    add(9.4,7.6);
    return 0;
}
*/

// C++ program to demonstrate constructor overloading


class Person {
   private:
    int age;

   public:
    // 1. Constructor with no arguments
    Person1() {
        age = 20;
    }

    // 2. Constructor with an argument
    Person(int a) {
        age = a;
    }

    int getAge() {
        return age;
    }
};

int main() {
     person1(45),person person2;

    cout << "Person1 Age = " << person1.getAge() << endl;
    cout << "Person2 Age = " << person2.getAge() << endl;

    return 0;
}
