//Default arguments
#include <iostream>
#include <iomanip>
using namespace std;

void print(char ch='-',int n=10);

int main()
{
  print();
  print('*');
  print('=',5);
}
void print(char ch, int n)
{
  for(int i=1;i<=n;i++)
  cout<<ch;
  cout<<endl;
}
