#include<iostream>
#include<iomanip>
using namespace std;
#define size 4

class queue
{
  int data[size];
  int front,rear;
public:
  queue()
  {
    front = 1;
    rear = 1;
  }
    void insert();
    void deletion();
    void display();
};
void queue::insert()
{
  if(rear == size - 1)
  {
    cout<<"\n queue is full";
  }
  else if(rear == -1)
  {
    rear++;
    front++;
  }
  else
  {
    rear++;
    cout<<"Enter Data : ";
    cin>>data[rear];
  }
}
void queue::deletion()
{
  if(front==-1)
  {
    cout<<"\nQueue is empty ";
  }
  cout<<data[front]<<" deleted"<<endl;
  if(front==rear)
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
  for(int i = front;i<=rear;i++)
  {
    cout<<data[rear];
  }
}
int main()
{
  queue q;
  int ch;
  do{
    cout<<"\n1. Insert\n2. Delete\n3. Display\n4. Quit\nEnter choice(1-3)"<<endl;
    cin>>ch;
    switch(ch)
    {
      case 1:q.insert();break;
      case 2:q.deletion();break;
      case 3:q.display();
    }
  }while(ch!=3);
}
