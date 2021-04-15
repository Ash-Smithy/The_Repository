#include <iostream>
#include <iomanip>
using namespace std;

class Base
{
  int a;
  public:
    void set_a()
    {
      cout << "Enter a value for a: ";
      cin >> a;
    }
    int get_a()
    {
      return a;
    }
};
class Derived: public Base
{
  int b,res;
public:
  void set_b()
  {
    cout<<"Enter a value for b: ";
    cin>>b;
  }
  void product()
  {
    res=b*get_a();
    cout << "Product is: " << res;
  }
};
int main()
{
  Derived obj;
  obj.set_a();
  obj.set_b();
  obj.product();
}
