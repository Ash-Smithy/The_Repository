#include <iostream>
using namespace std;

class A
{
  int a;
public:
  void set_a()
  {
    cout << "Enter a value: ";
    cin >> a;
  }
  int get_a()
  {
    return a;
  }
};
class B
{
  int b;
public:
  void set_b()
  {
    cout << "Enter b value: ";
    cin >> b;
  }
  int get_b()
  {
    return b;
  }
};
class C: public A, public B
{
  int c;
public:
  //set_a()
  //set_b()
  //get_a()
  //get_b()
  void add()
  {
    c=get_a()+get_b();
    cout << "Addition is: " << c;
  }
};
int main()
{
  C obj;
  obj.set_a();
  obj.set_b();
  obj.add();
  return 0;
}
