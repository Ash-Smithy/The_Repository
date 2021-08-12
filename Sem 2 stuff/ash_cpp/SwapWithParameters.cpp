#include <iostream>
#include <iomanip>
using namespace std;
void swap (int &x, int &y)
{
    int temp;
    temp = x;
    x = y;
    y = temp;
}
int main ()
{
    int a, b;
    a = 10;
    b = 20;
    cout << "Before swapping the values are " << a << " and " << b << endl;
    swap (a, b);
    cout << "After swapping the values are " << a << " and " << b << endl;
    return 0;
}
