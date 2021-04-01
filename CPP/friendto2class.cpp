#include<iostream>
#include<iomanip>
using namespace std;
class TWO;         //forward declaration
class ONE
{
private:
  int m;
public:
  void getm()
  {
    cout<<"Enter a value :: ";
    cin>>m;
  }
  friend int max(ONE o,TWO t); //function prototype taking two class parameters
};
class TWO
{
private:
  int n;
public:
  void getn()
  {
    cout<<"Enter a value : ";
    cin>>n;
  }
  friend int max(ONE o, TWO t);
};
int max(ONE o, TWO t)
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
  cout<<endl;
  t.getn();
  cout<<endl;
  cout<<"The max value is :: "<<max(o,t);
  return 0;
}
