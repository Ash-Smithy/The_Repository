//Trying out constructors

#include <iostream>
using namespace std;

class Table
{
public:
  string t,c;
  int n;
  Table(string a,string b, int z)
  {
    t=a;
    c=b;
    n=z;
    cout << "This is it " << t << " " << c << " " << n << endl;
  }
  Table(string a,string b)
  {
    t=a;
    c=b;
    cout << "This is another one " << t << " " << c << endl;
  }
  Table(string a)
  {
    t=a;
    cout << "This is one " << t << endl;
  }
};
int main()
{
Table("Big","Four", 4);
Table("Big");
Table("Big","Four");

return 0;
}
