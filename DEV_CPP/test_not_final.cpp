#include<iostream>
#include<iomanip>
using namespace std;
class number
{
private:
  int a,b,s1,s2;
public:
  int getdata(int m,int n);
  int sum();
  int sub();
  int show()
  {
    cout<<"\n Enter number 1 : ";
    cin>>a;
    cout<<"\nEnter number 2 : ";
    cin>> b;
    cout<<"\nAddition of the number is : "<<sum()<<endl;
    cout<<"\n Subtraction of the numbers is : "<<sub()<<endl;
  }
};
int number::getdata(int m,int n)
{
  a=m;
  b=n;
}
int number::sum()
{
  s1 = a+b;
}
int number::sub()
{
  s2 = a-b;
}
int main()
{
  number x;
  x.getdata(10,20);
  x.show();
  return 0;
}
