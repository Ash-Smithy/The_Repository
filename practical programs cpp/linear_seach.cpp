#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
  int arr[10]={5,3,7,23,8,2,9,4,2,1};
  int i,x;
  for(i=0;i<10;i++)
  {
    cout<<setw(3)<<arr[i]<<setw(3);
  }
  cout<<"\nEnter element to search :: ";
  cin>>x;
  for(i = 0 ;i< 10; i++)
  {
    if(arr[i] == x)
    {
      cout<<"element "<<x<<" found at position :: "<<i+1<<endl;
      break;
    }
    else if(i == 10 && arr[i]!=x)
    {
      cout<"\nElement not found in array\n";
    }
    else
    {
      continue;
    }
  }
  return 0;
}
