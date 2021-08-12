#include <iostream>
#include <iomanip>
using namespace std;
class Add
{
  int a,b;
public:
  Add(int x,int y=0)
  {
    a=x;
    b=y;
  }
  void show()
  {
    cout << "a = " << a << "\tb = " << b << endl;
  }
  ~Add()
  {
    cout << "Object is deleted" <<endl;
  }
};
int main()
{
  Add a1(5);
  Add a2(3,4);
  a1.show();
  a2.show();
  return 0;
}
