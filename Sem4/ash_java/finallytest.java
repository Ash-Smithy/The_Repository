//Program to implement finally statement
class finallytest
{
    public static void main(String args[])
    {
        int x=0;
        try 
        {
            int y=34/x;
        } 
        catch (Exception e) 
        {
          System.out.println("divisible by zero error");  
        }
        finally
        {
            int y=50/10;
            System.out.println("In finally answer is: "+y);
        }
    }
}