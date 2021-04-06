//here we'll create a private function and using public function use it in main
#include<iostream>
#include<iomanip>
using namespace std;

class value
{
private:
  int a,b;
  void getdata();
public:
  void show();
};
void value::getdata()
{
  cout<<"Enter num1 : ";
  cin>>a;
  cout<<"\nEnter num2 : ";
  cin>>b;
}
void value::show()
{
  getdata();
  cout<<"The Two numbers are :: "<<a<<" and "<<b<<endl;
}
int main()
{
  value obj;
  obj.show();
  return 0;
}
