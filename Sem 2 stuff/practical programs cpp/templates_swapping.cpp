#include<iostream>
#include<iomanip>
using namespace std;
template <class T>
void swap_1(T &x,T &y)
{
  T t;
  t = x;
  x = y;
  y = t;
}
void with_char()
{
  char ch1,ch2;
  cout<<"\nEnter character Values :: ";
  cin>>ch1>>ch2;
  swap_1(ch1,ch2);
  cout<<"\nAfter Swap :: ch1 = "<<ch1<<" ch2 = "<<ch2<<endl;
}
void with_int()
{
  int a,b;
  cout<<"\nEnter Integer Values :: ";
  cin>>a>>b;
  swap_1(a,b);
  cout<<"\nAfter Swap :: a = "<<a<<" b = "<<b<<endl;
}
void with_float()
{
  double a,b;
  cout<<"\nEnter Float Values :: ";
  cin>>a>>b;
  swap_1(a,b);
  cout<<"\nAfter Swap :: a = "<<a<<" b = "<<b<<endl;
}
int main()
{
  with_char();
  with_int();
  with_float();
  return 0;
}
