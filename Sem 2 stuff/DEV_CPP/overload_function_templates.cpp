#include<iostream>
#include<iomanip>
using namespace std;
template<class T>
void print(T data)
{
  cout<<data<<endl;
}
template<class T>
void print(T data, int ntimes)
{
  int i=1;
  for(i;i<ntimes;i++)
  {
    cout<<data<<endl;
  }
}
int main()
{
  print(1);
  print(1.5);
  print(520,2);
  print("OOP is Great",3);
  return 0;
}
