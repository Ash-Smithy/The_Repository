#include <iostream>
using namespace std;
class Add
{
  int x,y,z;
public:
  Add(int a,int b)
  {
    x=a;
    y=b;
  }
  Add()
  {
    x=0;
    y=0;
  }
  void show()
  {
    cout<<x<<"+i"<<y<<endl;
  }
  Add operator+(Add ob)
  {
    Add temp;
    temp.x=x+ob.x;
    temp.y=y+ob.y;
    return temp;
  }
};

int main()
{
  Add ob1(2,3),ob2(3,4),ob3;
  ob3=ob1+ob2;
  ob1.show();
  ob2.show();
  ob3.show();
  return 0;
}
