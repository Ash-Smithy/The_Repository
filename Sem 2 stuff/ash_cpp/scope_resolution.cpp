#include <iostream>
#include <iomanip>
using namespace std;

int m=10;
int main()
{
  int m = 20;
  cout << "m_logical= " << m << endl;
  cout << "m_global= " << ::m << endl;
  return 0;
}
