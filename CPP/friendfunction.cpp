//its a sin to use friendly functions in cpp
#include<iostream>
#include<iomanip>
using namespace std;
friend int friendly_func(int, int,int );
class test
{
private:
  int a,b,c;
public:
  void getdata()
    cout<<"ENter value for three variables : ";
    cin>>a>>b>>c;
    {
    cout<<endl;
  }
  void putdata()
  {
    cout<<"The numbers entered are : "<<endl;
    cout<<"A = "<<a<<endl<<"B = "<<b<<endl<<"C = "<<c<<endl;
  }
  friend int friendly_func(int a,int b,int c)
  {
    return a+b+c;
  }

};
