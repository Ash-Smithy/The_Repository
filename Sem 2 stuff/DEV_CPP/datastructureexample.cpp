//searching element in array
#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
  int arr1[10],n,i,search,pos,flag = 0;
  cout<<"Enter the no. of elements you want in the array :: ";
  cin>>n;
  cout<<"Enter the elements of the array now :: ";
  for(i=0;i<n;i++)
  {
    cin>>arr1[i];
  }
  cout<<"\nEnter the element you want to search in the array :: ";
  cin>>search;
  for(i=0;i<n;i++)
  {
    if(arr1[i]==search)
    {
      pos = i;
      flag = 1;
      break;
    }
  }
  if(flag == 1)
  {
    cout<<"Element "<<search<<" found at "<<pos+1<<" position of the array";
  }
  else
  {
    cout<<"Element "<<search<<" not found in the array ";
  }
  return 0;
}
