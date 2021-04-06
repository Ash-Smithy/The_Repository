#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
  int a = 100;
  int &ref = a;
  cout<<"Value of a is : "<<a<<endl;
  cout<<"value of ref is : "<<ref<<endl;
  cout<<"address of a is :: "<<&a<<endl;
  cout<<"address of ref is :: "<<&ref<<endl;
  return 0;
}
//same memory location but different names
