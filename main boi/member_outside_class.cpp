#include<iostream>
#include<iomanip>
using namespace std;
class item
{
private:
  int num,cost;
public:
  void getdata(int ,int );
  void putdata();
};
//main thing in this program is the scope resolution operator
void item::getdata(int a, int b)
{
  num = a;
  cost = b;
}
void item::putdata()
{
  cout<<num<<endl;
  cout<<cost<<endl;
}
int main()
{
  item obj;
  obj.getdata(10,20);
  obj.putdata();
  return 0;
}
