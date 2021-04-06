#include<iostream>
#include<iomanip>
using namespace std;
class item
{
  int num;
  float cost;
public:
  void getdata(int a, int b)
  {
    num = a;
    cost = b;
  }
  void putdata()
  {
    cout<<num<<endl;
    cout<<cost<<endl;
  }
};
int main()
{
  item obj;
  obj.getdata(10,20);
  obj.putdata();
  return 0;
}
