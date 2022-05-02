class test
{
    public static void main(String args[]) 
    {
        try
        {
            try
            {
                System.out.println("div by 0");
                int a=10/0;
            }
            catch (ArithmeticException r)
            {
                System.out.println("Exception caught inside");
            }
            try
            {
                int h[]= new int[5];
                h[5]=4;
            }
            catch (ArrayIndexOutOfBoundsException k)
            {
                System.out.println("Array Exception");
            }
        }
        catch (Exception e)
        {
            System.out.println("Handled Exception");
        }

    }
}