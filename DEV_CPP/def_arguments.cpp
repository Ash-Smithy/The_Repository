#include<iostream>
#include<iomanip>
using namespace std;
void print(char ch='-',int n=10);
int main()
{
  print();
  print('*');
  print('*',5);
}
void print(char ch, int n)
{
  int i;
  for(i=0;i<n;i++)
  {
    cout<<ch;
  }
  cout<<endl;
}
