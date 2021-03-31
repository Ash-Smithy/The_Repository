#include<iostream>
using namespace std;

class SUM
{
  int x;
public:
  void getdata(int m)
  {
    x=m;
  }
  SUM sum(SUM s)
  {
    SUM temp;
    temp.x=x+s.x;
    return(temp);
  }
  void show()
  {
    cout << "Answer is: " << x;
  }
};
int main()
{
  SUM s1,s2,s3;
  s1.getdata(4);
  s2.getdata(10);
  s3=s1.sum(s2);
  s3.show();
  return 0;
}
