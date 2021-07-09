#include<iostream>
#include<iomanip>
using namespace std;
class ADD
{
  int x,y;
public:
  ADD(int a,int b)
  {
    x = a;
    y = b;
  }
  ADD()
  {
    x=0;
    y=0;
  }
  void show()
  {
    cout<<"X = "<<x<< " Y = "<<y<<endl;
  }
  ADD operator+(ADD ob)
  {
    ADD temp;
    temp.x = x + ob.x;
    temp.y = y + ob.y;
    return temp;
  }
};
int main()
{
  ADD obj1(2,3),obj2(3,4),obj3;
  obj3 = obj1+obj2;
  obj1.show();
  obj2.show();
  obj3.show();
  return 0;
}
