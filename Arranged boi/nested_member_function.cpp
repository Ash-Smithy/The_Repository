#include<iostream>
#include<iomanip>
using namespace std;
class number
{
private:
  int a,b;
public:
  int sum();
  int sub();
  void show()
  {
    cout<<"Enter Number 1 : ";
    cin>>a;
    cout<<"\nEnter Number 2 : ";
    cin>>b;
    cout<<"the sum of the numbers is : "<<sum()<<endl;
    cout<<"The result of subtraction is : "<<sub()<<endl;
  }
};
int number::sum()
{
  return a+b;
}
int number::sub()
{
  return a-b;
}
int main()
{
  number obj;
  obj.show();
  return 0;
}
