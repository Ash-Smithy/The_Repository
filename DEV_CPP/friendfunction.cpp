//its a sin to use friendly functions in cpp
#include<iostream>
#include<iomanip>
using namespace std;
class test
{
private:
  int a,b,c;
public:
  void getdata()
  {
    cout<<"ENter value for three variables : ";
    cin>>a>>b>>c;
    cout<<endl;
  }
  void putdata()
  {
    cout<<"The numbers entered are : "<<endl;
    cout<<"A = "<<a<<endl<<"B = "<<b<<endl<<"C = "<<c<<endl;
  }
  friend int friendly_func(test t);

};
int friendly_func(test t)
{
  return int(t.a+t.b+t.c);
}
int main()
{
  test t1;
  t1.getdata();
  t1.putdata();
  cout<<"Sum of the numbers is : "<<friendly_func(t1);
}
