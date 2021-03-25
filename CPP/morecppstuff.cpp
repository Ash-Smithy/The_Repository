#include<iostream>
using namespace std;
class values{
  int a,b;
  void getdata()
  {
    cout<<"Enter two values : ";
    cin>>a>>b;
  }
public:
  void show()
  {
  getdata();
  cout<<"A = "<<a<<"\t"<<"B = "<<b<<endl;
  }
};
int main()
{
  values v;
  //v.getdata(); won't work directly since private
  v.show();
  return 0;
}
