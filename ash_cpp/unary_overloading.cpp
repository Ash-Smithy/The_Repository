#include <iostream>
using namespace std;

class UnaryOp
{
  int x,y,z;
public:
  UnaryOp(int a,int b, int c)
  {
    x=a;
    y=b;
    z=c;
  }
  void show()
  {
    cout<<x<<"\t"<<y<<"\t"<<z;
    cout<<endl;
  }
  void operator-()
  {
    x=-x;
    y=-y;
    z=-z;
  }
};
int main()
{
  UnaryOp un(10,-40,70);
  un.show();
  -un;
  un.show();
  return 0;
}
