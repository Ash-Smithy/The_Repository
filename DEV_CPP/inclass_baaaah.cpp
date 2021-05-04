#include<iostream>
#include<iomanip>

class A
{
private:
  int a,b,c,sum;
public:
  void getdata()
  {
    int x,y,z;
    std::cout<<"Enter 3 integers :: ";
    std::cin>>x>>y>>z;
    a = x;
    b = y;
    c = z;
  }
  void displaydata()
  {
    sum = a+b+c;
    std::cout<<"The sum of the three numbers is :: "<<sum;
  }
};
int main()
{
  A ob;
  ob.getdata();
  ob.displaydata();
  return 0;
}
