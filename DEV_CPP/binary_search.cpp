//binary search
#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
  int flag=0,n,lower_bound,upper_bound,middle_bound,x;
  n = 5;
  int temp;
  int arr[n]= {8,5,7,6,9};
  for(int i =0; i < n-1;i++)
  {
    for(int j = 0; j < n-i;j++)
    {
        if(arr[j]>arr[j+1])
        {
          temp = arr[j];
          arr[j] = arr[j+1];
          arr[j+1] = temp;
        }
    }
  }
  for(int i=0;i<n;i++)
  {
    cout<<setw(3)<<arr[i]<<setw(3);
  }
  cout<<endl;
  lower_bound = 0;
  upper_bound = n;
  cout<<"Enter the element to be searched :: ";
  cin>>x;
  while(flag!=1)
  {
    middle_bound = lower_bound+((upper_bound-lower_bound)/2);
    if(upper_bound<lower_bound)
    {
      cout<<"\nElement does not exist in the array"<<endl;
      break;
    }
    else if(arr[middle_bound]<x)
    {
      lower_bound=middle_bound+1;
    }
    else if(arr[middle_bound]>x)
    {
      upper_bound = middle_bound-1;
    }
    else if(arr[middle_bound]==x)
    {
      cout<<"element : "<<x<<" found at :: "<<middle_bound+1<<" postition";
      flag = 1;
    }
  }
  return 0;
}
