#include <iostream>
using namespace std;

class Base
{
public:
  virtual void print()
  {
    cout << "Base class";
  }
};
class Derived : public Base
{
public:
  void print()
  {
    cout << "Derived class";
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
