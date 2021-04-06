#include<iostream>
#include<iomanip>
using namespace std;
void swap(int , int);
void swap(int a,int b)
{
  int temp;
  temp = a;
  a = b;
  b = temp;
  cout<<"In function After swapping :: A == "<<a<<" B == "<<b<<endl;
}
int main()
{
  int a,b;
  a = 10;
  b = 20;
  cout<<"In main Before swapping :: A == "<<a<<" B == "<<b<<endl;
  swap(a,b);
  cout<<"In main After swapping :: A == "<<a<<" B == "<<b<<endl;
}
