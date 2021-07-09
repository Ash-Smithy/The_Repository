#include <iostream>
using namespace std;

class Shape
{
protected:
  int d1,d2;
public:
  void getdim()
  {
    cout << "Enter d1,d2 values: ";
    cin >> d1 >> d2;
  }
};

class Rectangle : public Shape
{
  float area;
public:
  void area_rect()
  {
    area=d1*d2;
    cout << "Area of rectangle: " << area <<endl;
  }
};
class Triangle: public Shape
{
  float area;
public:
  void area_tri()
  {
    area=0.5*d1*d2;
    cout << "Area of Triangle: " << area;
  }
};
int main()
{
  Rectangle hah;
  Triangle aha;
  hah.getdim();
  hah.area_rect();
  aha.getdim();
  aha.area_tri();
  return 0;
}
