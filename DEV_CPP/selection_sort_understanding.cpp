#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
  int arr[5]={20,12,10,15,2};
  int i,j,swap,n=5;

  for(i = 0;i<n;i++)
  {
    for(j=i-1;j<n;j++)
    {
      if(arr[j]<arr[j+1])
      {
        swap=arr[j];
        arr[j]=arr[j+1];
        arr[j+1]=swap;
      }
    }
  }
  cout<<"\nThe sorted list is :: "<<endl;
  for(i=0;i<n;i++)
  {
    cout<<setw(3)<<arr[i];
  }
  return 0;
}
