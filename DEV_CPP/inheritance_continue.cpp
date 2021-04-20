#include<iostream>
#include<iomanip>
using namespace std;
class A
{
protected:
  int n1;
public:
  void getn1()
  {
    cout<<"Enter n1 value : ";
    cin>>n1;
  }
};
class B:public A
{
protected:
  int n2;
public:
  void getn2()
  {
    cout<<"Enter n2 value : ";
    cin>>n2;
  }
};
class C:public B
{
  int sum;
public:
  void add()
  {
    sum = n1+n2;
    cout<<"Sum is : "<<sum;
  }
};
int not_main()
{
  C obj;
  obj.getn1();
  obj.getn2();
  obj.add();
  return 0;
}
class shape
{
protected:
  float d1,d2;
public:
  void getd()
  {
    cout<<"Enter the value for d1 and d2 :: "<<endl;
    cin>>d1>>d2;
  }
};
class Rectangle: public shape
{
  float area;
public:
  void arearect()
  {
    area = d1*d2;
    cout<<"Area of rectangle is :: "<<area<<endl;
  }
};
class Triangle: public shape
{
  float area;
public:
  void areatri()
  {
    area = 0.5*d1*d2;
    cout<<"Area of Triangle is :: "<<area<<endl;
  }
};
int not_main2()
{
  Rectangle r;
  Triangle t;
  r.getd();
  r.arearect();
  t.getd();
  t.areatri();
  return 0;
}
int main()
{
  not_main2();
  return 0;
}
