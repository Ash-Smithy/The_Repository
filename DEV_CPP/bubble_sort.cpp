#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
  int array[5] = { 5,4,1,2,3},n,c,d,swap;
  n = 5;
  for(c = 0; c < n-1 ; c++)
  {
    for(d = 0; d < n-c; d++)
    {
      if(array[d]>array[d+1])
      {
        swap = array[d];
        array[d]=array[d+1];
        array[d+1]=swap;
      }
    }
  }
  cout<<"sorted list in ascending order :: "<<endl;
  for(c=0;c<n;c++)
  {
    cout<<setw(5)<<array[c];
  }
  return 0;
}
