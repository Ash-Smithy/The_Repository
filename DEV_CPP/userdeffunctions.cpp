//Program to implement functions

#include<iostream>
#include<iomanip>
using namespace std;
int wow(int,int);
int main()
{
  int a,b;
  cout << "Enter two numbers: ";
  cin >> a >> b;
  cout << "Hakuna Matata values: " << wow(a,b);
  return 0;
}

int wow(int x,int y)
{
  return x+y;
}
