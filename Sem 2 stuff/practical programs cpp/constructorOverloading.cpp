#include <iostream>
#include <iomanip>
using namespace std;
class aha
{
  int x,y;
public:
  aha()
  {
    x=12;
    y=40;
  }
  aha(int a,int b)
  {
    x=a;
    y=b;
  }
  aha(aha &ob)
  {
    x = ob.x;
    y = ob.y;
  }
  void show()
  {
    cout << "The values: " << x << " " << y;
  }
};

int main()
{
  aha a1;
  aha a2(4,5);
  aha a3(a2);
  cout << "Value without arguments: ";
  a1.show();
  cout << "Value with arguments: ";
  a2.show();
  cout<<"Demonstrating Copy constructor :: ";
  a3.show();
  return 0;
}
