//q25 create class MAT of size mxn. Define all possible matrix operations for two matrix objects
#include<iostream>
#include<iomanip>
using namespace std;
class MAT
{
  int m,n;
  int arr[100][100];
public:
  MAT()
  {
    m = 2;
    n = 2;
  }
  MAT(int a,int b)
  {
    m = a;
    n = b;
  }
  void matrix_value();
  void display();
  void addition(MAT a,MAT b);
  void multiplication(MAT a,MAT b);
  void transpose();
};
void MAT::matrix_value()
{
  int i, j;
  for (i = 0; i < m; i++)
  {
    for (j = 0; j < n; j++)
    {
      cin>>arr[i][j];
    }
    cout<<endl;
  }
}
void MAT::transpose()
{
  int i, j;
  for (i = 0; i < m; i++)
  {
      for (j = 0; j < n; j++)
      {
          cout<<" "<<arr[j][i]<<" ";
      }
      cout<<"\n";
  }
}
void MAT::display()
{
  int i, j;
  for (i = 0; i < m; i++)
  {
      for (j = 0; j < n; j++)
      {
          cout<<" "<<arr[i][j]<<" ";
      }
      cout<<"\n";
  }
}
void MAT::addition(MAT o1,MAT o2)
{
  int i,j;
  for(i=0;i<m;i++)
  {
    for(j=0;j<n;j++)
    {
      arr[i][j]=o1.arr[i][j]+o2.arr[i][j];
    }
  }
  for (i = 0; i < m; i++)
  {
      for (j = 0; j < n; j++)
      {
          cout<<" "<<arr[i][j]<<" ";
      }
      cout<<"\n";
  }
}
void MAT::multiplication(MAT o1,MAT o2)
{
  int i,j,n,r2,c1,c2;
  r2 = o2.m;
  c2 = o2.n;
  c1 = o1.n;
  for (i = 0; i < r2; i++)
  {
      for (j = 0; j < c1; j++)
      {
          arr[i][j] = 0;

          for (n = 0; n < c2; n++)
          {
              arr[i][j] += o1.arr[i][n] * o2.arr[n][j];
          }
      }
  }
  for (i = 0; i < r2; i++)
  {
      for (j = 0; j < c1; j++)
      {
          cout<<" "<<arr[i][j]<<" ";
      }
      cout<<"\n";
  }
}
int main()
{
  int r1,c1,r2,c2,ch;
  cout<<"Enter the order for matrix 1 :: ";
  cin>>r1>>c1;
  cout<<"Enter the order for matrix 2 :: ";
  cin>>r2>>c2;
  MAT mat1(r1,c1);
  MAT mat2(r1,c2);
  MAT addobject(r1,c1);
  MAT multiplyobject(r1,c2);
  cout<<"Enter values for matrix 1 :: "<<endl;
  mat1.matrix_value();
  cout<<"Enter the values for matrix 2 :: "<<endl;
  mat2.matrix_value();
  do {
    cout<<"Enter choice :: \n1 for addition \n2 for displaying \n3 to print transpose of matrix \n4 for multiplication \n5 to quit \n::";
    cin>>ch;
    switch(ch)
    {
      case 1:
      if(r1==r2 && c1==c2)
      {
        cout<<"Addition result :: "<<endl;
        addobject.addition(mat1,mat2);
      }
      else
      {
        cout<<"\nThe orders are not equal thus addition not possible"<<endl;
      }
      break;
      case 2:
      cout<<"matrix 1  :: "<<endl;
      mat1.display();
      cout<<"matrix 2 :: "<<endl;
      mat2.display();
      break;
      case 3:
      cout<<"transpose of matrix 1 :: "<<endl;
      mat1.transpose();
      cout<<"Transpose of matrix 2 :: "<<endl;
      mat2.transpose();
      break;
      case 4:
      if(r1==c2)
      {
        cout<<"Multiplication result :: "<<endl;
        multiplyobject.multiplication(mat1,mat2);
      }
      else
      {
        cout<<"\nThe orders do not fulfill condition for multiplication"<<endl;
      }
      break;
    }
  }while(ch!=5);
  return 0;
}
