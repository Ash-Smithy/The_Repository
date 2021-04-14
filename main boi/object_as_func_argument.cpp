//can be done using two ways call by value and call by reference
//call by value --->>>
#include<iostream>
#include<iomanip>
using namespace std;
class square
{
  int x;
public:
  void getdata(int m)
  {
    x = m;
  }
  void answer(square s)
  {
    x = s.x*s.x;
  }
  void show()
  {
    cout<<"The square of the number you entered is : "<<x<<endl;
  }
};
int main()
{
  square obj1,obj2;
  obj1.getdata(6);
  obj2.answer(obj1);
  obj2.show();
  return 0;
}
