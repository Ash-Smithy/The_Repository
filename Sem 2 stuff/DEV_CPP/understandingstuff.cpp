#include<iostream>
#include<iomanip>
using namespace std;
#define size 4
class queue
{
private:
  int array[size];
  int front,rear;
public:
  queue()
  {
    front = -1;
    rear = -1;
  }
  void insert();
  void remove();
  void display();
};
void queue::insert()
{
  if(rear == size-1)
  {
    cout<<"The queue is full (data overflow condition arises)"<<endl;
    return;
  }
  else if(rear == -1)
  {
    rear++;
    front++;
  }
  else
  {
    rear++;
  }
  cout<<"enter value :: ";
  cin>>array[rear];
}
void queue::remove()
{
  if(front == -1)
  {
    cout<<"Empty queue"<<endl;
    return;
  }
  cout<<"Element "<<array[front]<<" removed";
  if(rear == front)
  {
    front = -1;
    rear = -1;
  }
  else
  {
    front++;
  }
}
void queue::display()
{
  cout<<"{ ";
  for(int i = front;i<=size-1;i++)
  {cout<<array[i]<<setw(5);}
  cout<<" }";
}
int main()
{
  queue q;
  int ch;
  do{
    cout<<"\nEnter choice :: ";
    cin>>ch;
    switch(ch)
    {
      case 1:q.insert();break;
      case 2:q.remove();break;
      case 3:q.display();break;
    }
  }while(ch!=4);
  return 0;
}
