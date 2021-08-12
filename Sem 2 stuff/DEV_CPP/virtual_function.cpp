#include<iostream>
#include<iomanip>
using namespace std;
class Base
{
public:
  virtual void print()
  {
    cout<<"Base class print function"<<endl;
  }
};
class Derived : public Base
{
public:
  void print()
  {
    cout<<"Derived class print function"<<endl;
  }
};
int main()
{
  Base *bptr;
  Derived d;
  bptr=&d;
  bptr->print();

  return 0;
}
