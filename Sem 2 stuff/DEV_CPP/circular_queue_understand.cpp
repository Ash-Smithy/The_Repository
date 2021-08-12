#include<iostream>
#include<iomanip>
using namespace std;
#define size 4
class queue
{
  int data[size],front, rear;
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
  if(rear == size-1 &&(front = 0||front == rear+1))
  {
    cout<<"\nCircular queue is full";
    return;
  }
  else if(rear == -1)
  {
    rear++;
    front++;
  }
  else if(rear == size-1)
  {
    rear = 0;
  }
  else
  {
    rear++;
  }
  cout<<"Enter Data : ";
  cin>>data[rear];
}
void queue::remove()
{
  if(front==-1)
  {
    cout<<"\nCircular queue is empty ";
    return;
  }
  cout<<data[front]<<"deleted"<<data[front]<<endl;
  if(front==rear)
  {
    front = -1;
    rear = -1;
  }
  else if(front ==size-1)
  {
    front=0;
  }
  else
  {
    front++;
  }
}
void queue::display()
{
  if(front<rear)
  {
    for(int i=front;i<=rear;i++)
    {
      cout<<data[i];
    }
  }
  else
  {
    for(int i = front;i<=size-1;i++)
    {
      cout<<data[i];
    }
  }
  for(int i=0;i<=rear;i++)
  {
    cout<<data[i];
  }
}
int main()
{
  queue q;
  int ch;
  do {
    cout<<"\n1. Insert\n2. Remove\n3. Display\n4. Exit"<<endl;
    cin>>ch;
    switch(ch)
    {
      case 1:q.insert();break;
      case 2:q.remove();break;
      case 3:q.display();break;
    }
  } while(ch!=4);
  return 0;
}
