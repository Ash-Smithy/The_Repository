#include<iostream>
#include<iomanip>
using namespace std;
class student
{
  int rno;
  char name[10];
  static char course[10];
public:
  void getdata()
  {
    cout<<"||ENTER A ROLL NO|| : ";
    cin>>rno;
    cout<<"||ENTER NAME|| : ";
    cin>>name;
  }
  void putdata()
  {
    cout<<"Roll no : "<<rno<<endl;
    cout<<"Name : "<<name<<endl;
    cout<<"Course : "<<course<<endl;
  }
};
char student :: course[10]="CSC";
int main()
{
  student s[10];//object array
  int i,n;
  cout<<"Enter how many student details you want to enter : ";
  cin>>n;
  for(i=0;i<n;i++)
  {
    s[i].getdata();
  }
  cout<<endl;
  cout<<"Now the details of the students you entered are :: ";
  for(i=0;i<n;i++)
  {
    s[i].putdata();
    cout<<endl;
  }
  return 0;
}
