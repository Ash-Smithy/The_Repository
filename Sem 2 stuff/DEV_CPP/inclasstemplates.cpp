#include<iostream>
#include<iomanip>
using namespace std;
const int size=3;
template <class T>
class vector
{

  T* v;
public:
  vector()
  {
    v = new T[size];
    for(int i=0;i<size;i++)
    v[i]=0;
  }
  vector(T* a)
  {
    for(int i=0;i<size;i++)
    v[i]=a[i];
  }
  T operator*(vector &y)
  {
    T sum = 0;
    for(int i = 0;i<size;i++)
    sum+=this->v[i]*y.v[i];
    return sum;
  }
};
int main()
{
  int x[3]=(1,2,3);
  int y[3]=(4,5,6);
  vectors<int> v1;
  vectors<int> v2;
  v1=x;
  v2=y;
  int r = v1*v2;
  cout<<"R = "<<r;
  return 0;
}
