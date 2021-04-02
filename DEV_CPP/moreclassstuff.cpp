#include<iostream>
#include<iomanip>
using namespace std;
class A
{
private:
  int a,b;
public:
  void input(int x,int y)
  {
    a=x;
    b=y;
  }
  void output()
  {
    cout<<"Addition is : "<<add()<<endl;
    cout<<"Subtraction is : "<<sub()<<endl;
  }
  int add()
  {
    return a+b;
  }
  int sub()
  {
    return a-b;
  }
};
int main()
{
  A obj;
  obj.input(7,8);
  obj.output();
  return 0;
}
