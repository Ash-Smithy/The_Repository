#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
  int a[4][4],sp[5][3];
  int i,j,k,t,p,n;
  cout <<"enter order of a matrix: ";
  cin>>p>>n;
  cout<<"Enter " << p*n << " Elements";
  for(i=0;i<p;i++)
  {
    for(j=0;j<n;j++)
    cin>>a[i][j];
  }
  k=1;
  t=0;
  for(i=0;i<p;i++)
  {
    for(j=0;j<n;j++)
    {
      if(a[i][j]!=0)
      {
        sp[k][0]=i;
        sp[k][1]=j;
        sp[k][2]=a[i][j];
        k++;
        t++;
      }
    }
  }
  sp[0][0]=p;
  sp[0][1]=n;
  sp[0][2]=t;
  cout<<"\n sparse matrix is:\n";
  for(i=0;i<=t;i++)
   {
     for(j=0;j<3;j++)
     {
       cout<<sp[i][j]<< " ";
     }
     cout<<"\n";
   }
}
