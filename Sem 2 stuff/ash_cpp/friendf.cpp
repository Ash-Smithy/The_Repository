//Friend to two classes
#include <iostream>
using namespace std;

class MEAN
{
  int n1,n2;
public:
  void getdata()
  {
    cout << "Enter a value: ";
    cin >> n1;
    cout << "Enter another value: ";
    cin >> n2;
  }
  friend float ans(MEAN m);
  friend int add(MEAN s);
};
float ans(MEAN m)
{
  return float(m.n1+m.n2)/2;
}
int add(MEAN s)
{
  return (s.n1+s.n2);
}
int main()
{
  MEAN m1;
  m1.getdata();
  cout << "Sum is: " << add(m1)<< endl;
  cout << "Mean is: " << ans(m1);
}
