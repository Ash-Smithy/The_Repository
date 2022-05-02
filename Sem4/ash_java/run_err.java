//Program to implement runtime error
class run_err
{
    public static void main(String args[])
    {
        int a=10;
        int b=5;
        int c=5;
        int x=1/(b-c);
        System.out.println("x= "+x);
        int y=1/(b+c);
        System.out.println("y= "+y);
    }
}