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
int main_3()
{
  item *p = new item[2];
  item *d = p;
  for(int i=0;i<2;i++)
  {
    p->getdata();
    p++;
  }
  for(int i=0;i<2;i++)
  {
    d->show();
    d++;
  }
  return 0;
}
int main()
{
  //cout<<"Method 1"<<endl;
  //main_1();
  //cout<<"\nMethod 2"<<endl;
  //main_2();
  cout<<"\nArray of objects :: \n";
  main_3();
  return 0;
}
