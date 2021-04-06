#include<iostream>
#include<iomanip>
using namespace std;
class Add
{
  int a,b;
public:
  Add(int x,int y=0)
  {
    a = 0;
    b = 0;
  }
  void show()
  {
    cout<<a<<endl;
    cout<<b<<endl;
  }
  ~Add()
  {
    cout<<"Object deleted "<<endl;
  }
};
int main()
{
  Add a1(5);
  Add a2(3,4);

  Add a3();
  {
    Add a4;
    a4.show();
  }
  a3.show();
  a1.show();
  a2.show();
  return 0;
}
