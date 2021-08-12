//template
#include<iostream>
#include<iomanip>
using namespace std;
template <class T1,class T2>
void display(T1 x,T2 y)
{
  cout<<x<<" "<<y<<endl;
}
int main()
{
  display(2023,"ACSC");
  display(2022,"NCSC");
  return 0;
}
