#include <iostream>
#include<iomanip>
using namespace std;
int main()
{
 int arr[] = { 12, 11, 13, 5, 6 },n = 5,i, key, j;
  for (i = 1; i < n; i++)
  {
    key = arr[i]; 
    j = i - 1;
    while (j >= 0 && arr[j] > key)
    {
      arr[j + 1] = arr[j];
      j = j - 1;
    }
  arr[j + 1] = key;
 }
 for (i = 0; i < n; i++)
 cout<< setw(4)<< arr[i];
 printf("\n");
 return 0;
}
