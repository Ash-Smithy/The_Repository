#include<iostream>
#include<iomanip>
using namespace std;
class mean
{
  int n1,n2;
public:
  void getdata()
  {
    cout<<"Enter num1 :: ";
    cin>>n1;
    cout<<"Enter num2 :: ";
    cin>>n2;
  }
  friend float ans(mean m);
};
float ans(mean m)
{
  return float (m.n1+m.n2)/2;
}
int main()
{
  mean m1,m2;
  m1.getdata();
  cout<<"\nThe mean of the numbers is :: "<<ans(m1);
  return 0;
}
