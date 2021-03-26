#include <iostream>
#include <iomanip>
using namespace std;

class student
{
  int rno;
  char name[10];
  static char course[10];
public:
  void getdata()
  {
    cout << "Enter roll number: ";
    cin >> rno;
    cout << "Enter name: ";
    cin >> name;
  }
  void putdata()
  {
    cout << "Student details" <<endl;
    cout << "Roll Number: " << rno <<endl;
    cout << "Name: " << name << endl;
    cout << "Course: " << course << endl;
  }
};
char student::course[10]="Cognitive";
int main()
{
    student s[10];
    int n;
    cout<<"Enter how many students you want: ";
    cin>>n;
    for (int i=0;i<n;i++)
     {
       s[i].getdata();
     }
    for (int i=0;i<n;i++)
     {
       s[i].putdata();
     }
     return 0;
}
