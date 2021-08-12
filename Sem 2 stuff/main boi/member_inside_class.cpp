#include<iostream>
#include<iomanip>
using namespace std;
class item
{
private:
  int num;
  float cost;
public:
  void getdata(int a=10, int b=20)
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
  obj.getdata();
  obj.putdata();
  return 0;
}
