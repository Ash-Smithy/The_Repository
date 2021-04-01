//Two friend functions
#include <iostream>
using namespace std;

class TWO;
class ONE
{
  int m;
public:
  void getm()
  {
    cout << "Enter a value: ";
    cin >> m;
  }
  friend int max(ONE o,TWO t);
};
class TWO
{
  int n;
public:
  void getn()
  {
    cout << "Enter a value: ";
    cin >> n;
  }
  friend int max(ONE o,TWO t);
};
int max(ONE o,TWO t)
{
  if(o.m>t.n)
  {
    return o.m;
  }
  else
  {
    return t.n;
  }
}

int main()
{
  ONE o;
  TWO t;
  o.getm();
  t.getn();
  cout << "Max value is: " << max(o,t);
  return 0;
}
