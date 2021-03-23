/* Function Overload */
#include <iostream>
#include <iomanip>
using namespace std;

int add(int ,int );
double add(double ,double );
int add(int ,int ,int );
int main()
{
  cout << "Function with two integer arguments: " << add(5,6)<<endl;
  cout << "Function with two double arguments: " << add(4.0,6.5)<<endl;
  cout << "Function with three integer arguments: " << add(5,5,5);
  return 0;
}

int add(int x,int y)
{
  return x+y;
}
double add(double x,double y)
{
  return x+y;
}
int add(int x, int y, int z)
{
  return x+y+z;
}

//On using float instead of double, we receieve an error. This is because the datatype gets converted 
