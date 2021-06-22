#include<iostream>
#include<iomanip>
using namespace std;
//creating the queue
#define size 4
class queue
{
  int array[size];
  int front,rear;
public:
  queue()
  {
    front = -1;
    rear = -1;
  }
  void display();
  void insert();
  void deletion();
};
void queue::insert()
{
  if(rear == size-1)
  {
    cout<<"\nThe queue is full!";
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
  cout<<"Enter Data to be inserted :: ";
  cin>>array[rear];
}
void queue::deletion()
{
  if(front==-1)
  {
    cout<<"\nThe queue is empty!";
    return;
  }
  cout<<array[front]<<" deleted!"<<endl;
  if (front==rear)
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
  cout<<"\n{ ";
  for(int i=front;i<=rear;i++)
  {
    cout<<" "<<array[i];
  }
  cout<<" }"<<endl;
}
int main()
{
  queue q;
  int ch;
  do {
    cout<<"\nSelect choice (1-3) :: \n1. insert \n2. delete \n3. display \n4. quit"<<endl;
    cin>>ch;
    switch(ch)
    {
      case 1:q.insert();break;
      case 2:q.deletion();break;
      case 3:q.display();
    }
  } while(ch!=4);
  return 0;
}
