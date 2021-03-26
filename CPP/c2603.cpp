//Such a bullly
#include<iostream>
static int count;
class test
{
  int code;
  static int count;
public:
  void setcode()
  {
    code = ++count;
  }
  void showcode()
  {
    cout<<"Object number : "<<code<<endl;
  }
  static void showcount()
  {
    cout<<"count : "<<count;
  }
};
int test::count;
int main()
{
  test t1,t2;
  t1.setcode();
  t2.setcode();
  test::showcount();
  test t3;
  t3.setcode();
  test::showcount();
  t1.showcount();
  t2.showcount();
  t3.showcount();
  return 0;
}
