#include<iostream>
#include<iomanip>
using namespace std;

class unaryOP
{
  int x,y,z;
public:
  unaryOP(int a, int b,int c)
  {
    x = a;
    y = b;
    z = c;
  }
  void show()
  {
    cout<<x<<"\t"<<y<<"\t"<<z<<endl;
  }
  void operator -()
  {
    x = -x;
    y = -y;
    z = -z;
  }
};
int main()
{
  unaryOP un(10,20,-30);
  un.show();
  -un;
  un.show();
  
  return 0;
}
