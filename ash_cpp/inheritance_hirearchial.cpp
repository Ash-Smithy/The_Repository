#include <iostream>
using namespace std;

class A
{
protected:
  int m1;
public:
  void getm1()
  {
    cout << "Enter a value: ";
    cin >> m1;
  }
};

class B : public A
{
protected:
  int m2;
public:
  void getm2()
  {
    cout << "Enter a value: ";
    cin >> m2;
  }
};
class C: public B
{
  int sum
}
