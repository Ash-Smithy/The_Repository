#include <iostream>
#include <iomanip>
using namespace std;

class MEAN
{
    int n1,n2;
  public:
    void getdata()
    {
      cout << "Enter a number: ";
      cin >> n1;
      cout << "Enter another number: ";
      cin >> n2;
    }
    friend float ans(MEAN m);
};
float ans(MEAN m)
{
  return float (m.n1+m.n2)/2;
}
int main()
{
  MEAN m1;
  m1.getdata();
  cout << "Mean is: " << ans(m1) << endl;

  MEAN m2;
  m2.getdata();
  cout <<" Lol: " << ans(m2) << endl;
}
