import MyPackage.balance;

public class account_bal 
{
    public static void main(String args[])
    {
        balance current[]=new balance[3];
        current[0]=new balance("John",15230.50);
        current[1]=new balance("Angelo",350.50);
        current[2]=new balance("Kim",-130.50);
        for(int i=0;i<3;i++){
            current[i].show();
        }
    }
}
