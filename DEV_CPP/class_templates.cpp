#include<iostream>
#include<iomanip>
using namespace std;
template <class T1,class T2>
class Test
{
private:
  T1 a;
  T2 b;
public:
  Test(T1 x,T2 y)
  {
    a = x;
    b = y;
  }
  void show()
  {
    cout<<"A = "<<a<<" B = "<<b<<endl;
  }
};
int main()
{
  Test<float, int> test1(1.5,5);
  Test<char, double> test2('a',5.55);
  test1.show();
  test2.show();
  return 0;
}
