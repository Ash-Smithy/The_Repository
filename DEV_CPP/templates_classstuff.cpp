#include<iostream>
#include<iomanip>
using namespace std;
template<class T1,class T2>
class Test
{
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
    cout<<a<<" "<<b<<endl;
  }
};
int main()
{
  Test<float, int> test1(1.23,123);
  Test<int, char> test2(24,'w');
  test1.show();
  test2.show();
  return 0;
}
