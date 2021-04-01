#include<iostream>
#include<iomanip>
using namespace std;
//return by reference means that a reference variable is used which reflects the changes in the original variable
int & max(int &x,int &y);
int main()
{
  int a,b;
  cout<<"Enter two integers :: ";
  cin>>a>>b;
  max(a,b)=425;
  cout<<"a = "<<a<<" b = "<<b<<endl;
  return 0;
}
int & max(int &x,int &y)
{
  if(x>y)
  {
    return x;
  }
  else
  {
    return y;
  }
}
