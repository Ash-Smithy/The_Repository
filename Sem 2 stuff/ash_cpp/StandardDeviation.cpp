#include <iostream>
#include <cmath>
using namespace std;
int main()
{
   float val[5] = {12.5, 7.0, 10.0, 7.8, 15.5};
   float sum = 0, mean, var = 0, stdv;
   int i;
   for(i = 0; i < 5; ++i)
    {
      sum += val[i];
    }
    mean = sum/5;
   for(i = 0; i < 5; ++i)
   var += pow(val[i] - mean, 2);
   var=var/5;
   stdv = sqrt(var);
   cout<<"The data values are: ";
   for(i = 0; i < 5; ++i)
   cout<< val[i] <<" ";
   cout<<endl;
   cout << "Variance is: " << var << endl;
   cout<<"Standard deviation of these data values is "<<stdv;
   //dev was here
}
