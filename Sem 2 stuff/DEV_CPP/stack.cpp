#include<iostream>
#include<iomanip>
using namespace std;
int stack[100],n=100,top = -1;
void push(int val)
{
  if(top >= n-1)
  {
    cout<<"\nStack is full, more would create data overflow condition\n";
  }
  else
  {
    top++;
    stack[top]=val;
  }
}
void pop()
{
  if(top <=-1)
  {
    cout<<"\nStack underflow condition\n";
  }
  else
  {
    cout<<"\nelement "<<stack[top]<<" popped\n";
    top--;
  }
}
void display()
{
  if(top<=-1)
  {
    cout<<"\nstack is empty\n";
  }
  else
  {
    int i;
    cout<<endl;
    for(i=top;i>=0;i--)
    {
      cout<<setw(3)<<stack[i]<<setw(3);
    }
    cout<<endl;
  }
}
int main()
{
  int ch,val;
  do {
    cout<<"Enter choice 1 for push 2 for pop 3 for display 4 to exit :: ";
    cin>>ch;
    switch(ch)
    {
      case 1:
      {
        cout<<"enter value to insert :: ";cin>>val;
        push(val);
        break;
      }
      case 2:pop();break;
      case 3:display();break;
    }
  } while(ch!=4);
}
