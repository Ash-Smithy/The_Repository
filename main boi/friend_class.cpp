#include<iostream>
#include<iomanip>
using namespace std;
class A
{
private:
  int a,b;
public:
  void get()
  {
    cout<<"Enter a and b :: ";
    cin>>a>>b;
  }
  friend class B;
};
class B
{
public:
  void ans(A ob)
  {
    int sum;
    sum = ob.a+ob.b;
    cout<<"\n"<<sum;
  }
};
int main()
{
  A ob1;
  B b;
  ob1.get();
  b.ans(ob1);
  return 0;
}
