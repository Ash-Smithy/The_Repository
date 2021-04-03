//basic structure/syntax of a class

#include<iostream>
#include<iomanip>
using namespace std;
class class_name        //class declaration
{
//#members of class : data members and member functions
private:   //member can be private
  //generally, variables are declared in private section
  int a,b,c;
public:    //member can be public
  //generally, functions are declared in public section
  void input()
  {
    cout<<"Enter two values : ";
    cin>>a>>b;
  }
  void calculate()
  {
    c = a+b; //member function can have an access to the private data of class
  }
  void output()
  {
    cout<<"A = "<<a<<endl;
    cout<<"B = "<<b<<endl;
    cout<<"sum C = "<<c<<endl;
  }
};
int main()
{
  class_name obj;  //class variable
  //to access the members of the class
  obj.input();    //message passing
  obj.calculate();
  obj.output();   //accessible outside the class
  /*
  obj.a(); is incorrect as a is declared as private and
  these members cannot be accessed outside the class
  */
  return 0;
}
//like structure and union a ; must be present at the end

/*
class class_name
{
private:
data members declaration
member function declaration
public:
data members declaration
member function declaration
};
 */
