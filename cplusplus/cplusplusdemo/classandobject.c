#include<iostream>
using namespace std;
class arithmetic
{
 public
 int a,b;
 void getdata()
 {
     cout<<"enter the value of a:="
     cin>>a;
     cout<<"enter the value of b:="
     cin>>b;

 }
 void arithmetic_op()
 {

     cout<<"The Addition is="<<(a+b)<<endl;
     cout<<"The Subtraction is="<<(a-b)<<endl;
     cout<<"The Multiplication is="<<(a*b)<<endl;
     cout<<"The Division ="<<(a/b)<<endl;
     cout<<"The modulation is="<<(a%b)<<endl;

};
void main()
{

    arithmetic obj;
    obj.getdata();
    obj.arithmetic.op();
    getch();
}
