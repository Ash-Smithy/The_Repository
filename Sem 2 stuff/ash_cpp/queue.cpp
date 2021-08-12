#include <iostream>
#include <iomanip>
#define size 4
using namespace std;

class queue
{
  int data[size];
  int front,rear;
public:
  queue()
  {
    front=-1;
    rear=-1;
  }
  void insert();
  void deletion();
};
void queue::insert()
{
  if(rear==size-1)
  {
    cout <<"\n queue is full";
    return;
  }
  else if(rear==-1)
  {
    rear++;
    front++;
  }
  else rear++;
  cout << "Enter Data: ";
  cin>>data[rear];
}
void queue::deletion()
{
  if(front==-1)
  {
    cout << "\n Queue is empty";
    return;
  }
  cout<<data[front]<<"deleted" <<endl;
  if (front==rear)
  {
    front=-1;
    rear=-1;
  }
  else front++;
}
void display()
{
  for(int i=front;i<=rear;i++)
  cout <<data [rear];
};
void main()
{
  queue q;
  int ch;
  do {
    cout<<"\n1.Insert\n2.Delete\n3.Display\n4.Quit\nEnter choice: ";
    cin>>ch;
    switch(ch)
    {
      case 1: q.insert();break;
      case 2: q.deletion();break;
      case 3: q.display();
    }
  }
  while(ch!=3);
}
