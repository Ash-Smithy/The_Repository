#include <iostream>
#include <iomanip>
using namespace std;
class tp
{
  int x,y;
public:
  tp()
  {
    x=0;
    y=0;
  }
  tp(int a, int b)
  {
    x=a;
    y=b;
  }
  tp operator+(tp ya)
  {
    tp temp;
    temp.x=x+ya.x;
    temp.y=y+ya.y;
    return temp;
  }
  void show()
  {
    cout << " " << x << " " << y << endl;
  }
};
int main()
{
  tp ob1(2,2),ob2(3,4),ob3;
  ob3=ob1+ob2;
  ob1.show();
  ob2.show();
  ob3.show();
  return 0;
}

