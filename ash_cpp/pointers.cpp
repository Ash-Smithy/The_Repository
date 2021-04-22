#include <iostream>
using namespace std;

class item
{
  float price;
  int code;
public:
  void getdata()
  {
  cout << "Enter values for code and price: ";
  cin >> code >> price;
  }
  void show()
  {
  cout <<"Code: " << code <<endl;
  cout << "Price: " << price;
  }
};


int main()
{
  item x,*ptr; //item *ptr=new item;
  ptr=&x;
  ptr->getdata(); //(*ptr).getdata()
  ptr->show(); //(*ptr).show()
  return 0;
}
