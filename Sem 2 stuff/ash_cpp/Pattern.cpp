/* Program to print the pattern as:
1
22
333
4444
55555*/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
  int a,i,j;
  cout << "Enter a number: ";
  cin >> a;
  for (i=0;i<=a;i++)
  {
    for (j=1;j<=i;j++)
    {
      cout << i;
    }
    cout << endl;
  }
  return 0;
}
