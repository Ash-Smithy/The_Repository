#include <iostream>
using napesapce std;

class Base
{
public:
  int b;
  void show()
  {
    cout << "b = " << b << endl;
  }
};
class Dervied : public Base
{
  pubilc:
  int d;
  void show()
  {
    cout << "b = " << endl << "d = " << d;
  }
};
int main()
{
  Base *bptr;
  Base b;
  bptr=&b;
  bptr->b=100;
  bptr->show();
  Derived d;
  bptr=&d;
  bptr->b=200;
  ((Derived *)bptr)->d=300;
  bptr->show();
  ((Derived *)bptr)->show();

  return 0;
}
