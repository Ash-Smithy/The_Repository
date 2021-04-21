#include<iostream>
#include<iomanip>
#include<string.h>
using namespace std;
template<class T>
T max(T &a,T &b)
{
  if(a>b)
  {
    return a;
  }
  else
  {
    return b;
  }
}
char *max(char *a, char *b)
{
  if (strcmp(a,b)>0)
  {
    return a;
  }
  else
  {
    return b;
  }
}
int main()
{
  char ch1,ch2,ch;
  cout<<"Enter two char values :: ";
  cin>>ch1>>ch2;
  ch = max(ch1,ch2);
  cout<<"The larger/max character is :: "<<ch<<endl;
  int a,b,c;
  cout<<"Enter two integer values :: ";
  cin>>a>>b;
  c = max(a,b);
  cout<<"The max integer is :: "<<c<<endl;
  return 0;
}
