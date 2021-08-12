#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
  int array[5]={2,6,5,8,4},n=5,i,j,swap,pos;
  for(i=0;i<n-1;i++)
  {
    pos = i;
    for(j=i+1;j<n;j++)
    {
      if(array[pos]>array[j])
      {
        pos = j;
      }
      if(pos!=i)
      {
        swap = array[i];
        array[i]=array[pos];
        array[pos]=swap;
      }
    }
  }
  cout<<"sorted array is : \n";
  for(i=0;i<n;i++)
  {
    cout<<setw(5)<<array[i];
  }
}
