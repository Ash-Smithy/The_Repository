//
#include <iostream>
#include <iomanip>
using namespace std;

class A
{
  int number;
  float cost;
public:
  void input(int x,float y)
{
  number = x;
  cost = y;
}
void output()
{
  cout << "number: " << number << endl;
  cout << "Cost: " << cost << endl;
}
};
int main()
{
  A obj; //A is a userdefined and obj is variable of the class
  obj.input(7,10.25);
  obj.output();
  return 0;
}
