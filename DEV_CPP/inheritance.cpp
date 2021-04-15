#include<iostream>
#include<iomanip>
using namespace std;
class Base
{
  int a;
public:
  void set_a()
  {
    cout<<"Enter a value for a :: ";
    cin>>a;
  }
  int get_a()
  {
    return a;
  }
};
class derived : public Base
{
  int b,res;
public:
  void set_b()
  {
    cout<<"Enter a value for b :: ";
    cin>>b;
  }
  void product()
  {
    res = b * get_a();
    cout<<"The result is :: "<<res<<endl;
  }
};
int main()
{
  derived ob1;
  ob1.set_a();
  ob1.set_b();
  ob1.product();
  return 0;

}
