public class Arith{
    public static void main(String args[])
    {
        int x = 10;
        int y = 25;
        int z = x+y;
        System.out.println("Sum of x and y (x+y) : "+z);
        int d = y-x;
        System.out.println("Difference of y and x (y-x) : "+d);
        int p = x*y;
        System.out.println("Product of x and y (x*y) : "+p);
        int q = y/x;
        System.out.println("Quotient of y and x (y/x) : "+q);
        int r = y%x;
        System.out.println("Remainder of y and x (y%x) : "+r);
    }
}