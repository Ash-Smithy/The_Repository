#include <iostream>
using namespace std;

class UnaryOp
{
  int x,y,z;
public:

  UnaryOp()
  {
    x=0;
    y=0;
    z=0;
  }
  UnaryOp(int a,int b, int c)
  {
    x=a;
    y=b;
    z=c;
  }
};
void UnaryOp :: operator- ()
{
  x=-x;
  y=-y;
  z=-z;
}
int main()
{
  UnaryOp un(10,-40,70);
  cout << "\n\nNumbers are:::\n";
  un.display();
  -un;
  cout <<"\n\nNumbers are after overloaded minus (-) operator :::\n";
  undisplay();
  return 0;
}
