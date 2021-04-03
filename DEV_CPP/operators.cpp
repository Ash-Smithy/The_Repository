//note :: all C operators are valid in cpp
#include<iostream>
#include<iomanip>
using namespace std;
//new cpp operators
/*
<< insertion operator
>> extraction operator
:: scope resolution operator
::*
->*
.*
endl
delete
new
setw
*/

// operator 1 --> scope resolution operator
int m=10;
void scope_resolution1();
void scope_resolution1()
{
  int m = 20;
  cout << "m_logical= " << m << endl;
  cout << "m_global= " << ::m << endl;
}

// operator 2 --> Memory management operator
void mem_mgmt_new();
void mem_mgmt_new()
{
int *p = new int;
float *q = new float;
*p = 25;
*q = 7.5;

cout<<sizeof(*p)<<endl;
cout<<sizeof(*q)<<endl;

}
void mem_mgmt_new_other();
void mem_mgmt_new_other()
{
  int *p = new int(25);
  float *q = new float(7.5);
  cout<<sizeof(p)<<endl;
  cout<<sizeof(q)<<endl;
}

//main()
int main()
{
  scope_resolution1();
  mem_mgmt_new();
  mem_mgmt_new_other();
}
