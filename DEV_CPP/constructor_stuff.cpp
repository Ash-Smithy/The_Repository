#include<iostream>
#include<iomanip>
using namespace std;
class A
{
  int a,b;
public:
  A()
  {
    a = 10;
    b = 20;
  }
  void show()
  {
    cout<<"A = "<<a<<endl;
    cout<<"B = "<<b<<endl;
  }
};
int main()
{
  A obj;
  obj.show();
}
