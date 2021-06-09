#include<iostream>
#include<iomanip>
using namespace std;

class bank_account
{
private:
  int acc_number,balance_amt=0;
  char name_of_depositor[300], type_of_account[500];
public:
  void initialize();
  void deposit();
  void withdraw();
  void display();
};
void bank_account::initialize()
{
  cout<<"\nEnter the name of depositor :: ";
  cin>>name_of_depositor;
  cout<<"\nEnter the type of account :: ";
  cin>>type_of_account;
  cout<<"\nEnter the account number :: ";
  cin>>acc_number;
  cout<<"\nEnter the balance amount :: ";
  cin>>balance_amt;
}
void bank_account::deposit()
{
  int amt_dep;
  cout<<"Account balance :: "<<balance_amt;
  cout<<"enter the amount to deposit :: ";
  cin>>amt_dep;
  balance_amt = balance_amt+amt_dep;
  cout<<"Account Balance after deposit :: "<<balance_amt;
}
void bank_account::withdraw()
{
  int amt_withdraw;
  cout<<"Account balance :: "<<balance_amt;
  cout<<"enter the amount to withdraw :: ";
  cin>>amt_withdraw;
  balance_amt = balance_amt-amt_withdraw;
  cout<<"Account Balance after withdrawing :: "<<balance_amt;
}
void bank_account::display()
{
  cout<<"The account details are - "<<endl;
  for(int i=0;i<10;i++)
  {
    cout<<"-";
  }
  cout<<"\nAccount holder name :: "<<name_of_depositor<<endl;
  cout<<"Account number :: "<<acc_number<<endl;
  cout<<"Account type :: "<<type_of_account<<endl;
  cout<<"Account balance :: "<<balance_amt<<endl;
  for(int i=0;i<10;i++)
  {
    cout<<"-";
  }
}
int main()
{
  bank_account b;
  int choice,i;
  b.initialize();
  labelchoice:
    {
      cout<<"Enter choice :: \n1 to display account details \n2  to deposit \n3 to withdraw";
      cin>>choice;
    }
  for(i=1;i<=1;i++)
  {
    if (choice == 1)
    {
      b.display();
      cout<<"\nTo select other options enter R else press any other key :: ";
      char choice2;
      cin>>choice2;
      if(choice2=='r' || choice2=='R')
      {
        goto labelchoice;
      }
      else
      break;
    }
    else if (choice == 2)
    {
      b.deposit();
      cout<<"\nTo select other options enter R else press any other key :: ";
      char choice2;
      cin>>choice2;
      if(choice2=='r' || choice2=='R')
      {
        goto labelchoice;
      }
      else
      break;
    }
    else if (choice == 3)
    {
      b.withdraw();
      cout<<"\nTo select other options enter R else press any other key :: ";
      char choice2;
      cin>>choice2;
      if(choice2=='r' || choice2=='R')
      {
        goto labelchoice;
      }
      else
      break;
    }
    else
    cout<<"Enter a valid value";
  }
  return 0;
}
