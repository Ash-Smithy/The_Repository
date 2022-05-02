//Program to implement try and catch statements
class try_catch
{
    public static void main(String args[])
    {
        int a=10;
        int b=5;
        int c=5;
        int x,y;
        try
        {
            x=a/(b-c);
        }
        catch(ArithmeticException e)
          {
            System.out.println("Division by Zero ");
          }
        y=a/(b+c);
        System.out.println("y= "+y);
    }
}