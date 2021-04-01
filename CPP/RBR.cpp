//Return by reference
#include <iostream>
#include <iomanip>
using namespace std;
int & max(int &x,int &y);
int main()
{
  int a,b,c;
  cout << "Enter two integers: ";
  cin >> a >> b;
  max(a,b)=425;
  cout << "a=" << a << "\nb="<<b;
  return 0;
}

int & max(int &x, int &y)
{
  if (x>y)
  return x;
  else
  return y;
}
