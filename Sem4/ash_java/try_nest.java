//program to implment nesting of try block
class try_nest
{
    public static void main(String main[])
    {
        try{
            System.out.println("outer blick starts");
            try
            {
                System.out.println("Inner block starters");
                int res=5/0;
            }
            catch(Exception e)
            {
                System.out.println("Input exception caught");
            }
            finally
            {
                System.out.println("Inner finallly");
            }
        }
        catch(Exception e)
        {
            System.out.println("Exception caught");
        }
        finally
        {
            System.out.println("outer Finally");
        }
    }
}