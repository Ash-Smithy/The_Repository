#include <iostream>
using namespace std;
class Sample
{
float real,imag;
public:
Sample()
{
 real=0.0;
 imag=0.0;
}
 Sample(float r, float i)
{
 real=r;
 imag=i;
}
friend Sample operator+(Sample,Sample);
void print()
{
  cout<<real<<"+i"imag;
}
};

Sample operator+(Sample p,Sample q)
{
  Sample temp;
  temp.real=p.real+q.real;
  temp.imag=p.imag+q.imag;
  return temp;
}
int main()
{
  Sample C1(3.5,1.1),C2(2.4,1.6),C3;
  C3=
}
