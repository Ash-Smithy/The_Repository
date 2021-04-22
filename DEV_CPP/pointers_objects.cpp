#include <iostream>
#include <iomanip>
using namespace std;
class item
{
  float price;
  int code;
public:
  void getdata()
  {
    cout<<"Enter value for code and price :: ";
    cin>>code>>price;
  }
  void show()
  {
    cout<<"Code :: "<<code<<endl;
    cout<<"Price :: "<<price<<endl;
  }
};
int main_1()
{
  item x,*ptr;
  ptr = &x;
  ptr-> getdata();
  (*ptr).show();
  return 0;
}
int main_2()
{
  item *ptr = new item;
  ptr->getdata();
  ptr->show();
  return 0;
}
int main()
{
  cout<<"Method 1"<<endl;
  main_1();
  cout<<"\nMethod 2"<<endl;
  main_2();
  return 0;
}
