#include<iostream>
#include<iomanip>
using namespace std;
class BASE
{
private:
  int x;
public:
  int get_x()
  {
    cout<<"Enter the values for X :: ";
    cin>>x;
    return x;
  }
};
class derived_1:public BASE
{
private:
  int y;
public:
  int get_y()
  {
    cout<<"Enter the value of Y :: ";
    cin>>y;
    return y;
  }
  void show()
  {
    cout<<"The sum of the values is :: "<<get_x+get_y<<endl;
  }
};
int main()
{
  derived_1 obj;
  obj.get_x();
  obj.get_y();
  obj.show();
  return 0;
}
