#include <iostream>
using namespace std;

class Base
{
public:
  virtual void draw()=0;
};
class Derived1 : public Base
{
public:
  void draw()
  {
    cout << "Derived1 class" << endl;
  }
};
class Derived2 : public Base
{
public:
  void draw()
  {
    cout << "Derived2 class" << endl;
  }
};
int main()
{
  Base *bptr;
  Derived1 d;
  bptr=&d;
  bptr->draw();
  Derived2 c;
  bptr=&c;
  bptr->draw();
  return 0;
}
