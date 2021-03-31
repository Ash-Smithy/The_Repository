#include <iostream>
using namespace std;


float ans(MEAN m)
{
  return float(m.n1+m.n2)/2;
}
int main()
{
  MEAN m1;
  m1.getdata();
  cout << "Answer is: " << ans(m1);
}
