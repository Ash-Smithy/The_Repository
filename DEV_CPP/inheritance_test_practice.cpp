#include<iostream>
#include<iomanip>
#include<windows.h>
using namespace std;
class BASE
{
private:
  int x;
public:
  void set_x()
  {
    cout<<"Enter the values for X :: ";
    cin>>x;
  }
  int get_x()
  {
    return x;
  }
};
class derived_1:public BASE
{
private:
  int y;
public:
  void get_y()
  {
    cout<<"Enter the value of Y :: ";
    cin>>y;
  }
  void show()
  {
    int result;
    result=get_x()+y;
    cout<<"The sum of the values is :: "<<result<<endl;
  }
};
class derived_2:private BASE
{
private:
  int y,res;
public:
  void get_y()
  {
    set_x();
    cout<<"enter the value of Y :: ";
    cin>>y;
  }
  void product()
  {
    res = get_x() * y;
    cout<<"The product of the numbers is :: "<<res<<endl;
  }
};
int main()
{
  derived_1 obj;
  cout<<"Using public inheritance :: "<<endl;
  int c = 3;
  while(c-- >0)
  {
    cout<<".\n";
    Sleep(1000);
  }
  obj.set_x();
  obj.get_y();
  obj.show();
  c = 3;
  while(c-- >0)
  {
    cout<<".\n";
    Sleep(1000);
  }
  derived_2 ob;
  ob.get_y();
  ob.product();

  return 0;
}
