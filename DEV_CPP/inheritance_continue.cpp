#include<iostream>
#include<iomanip>
using namespace std;
class A
{
protected:
  int n1;
public:
  void getn1()
  {
    cout<<"Enter n1 value : ";
    cin>>n1;
  }
};
class B:public A
{
protected:
  int n2;
public:
  void getn2()
  {
    cout<<"Enter n2 value : ";
    cin>>n2;
  }
};
class C:public B
{
  int sum;
public:
  void add()
  {
    sum = n1+n2;
    cout<<"Sum is : "<<sum;
  }
};
int main()
{
  
}
