//Finding greatest of three numbers

public class great_three {
    public static void main(String args[])
    {
        int a=56,b=65,c=93;
        if (a==b && a==c)
        {
            System.out.println("The numbers are equal");
        }
        else if (a>b && a>c)
        {
            System.out.println(a+" is the greatest");
        }
        else if (b>c)
        {
            System.out.println(b+" is the greatest");
        }
        else
        {
            System.out.println(c+" is the greatest");
        }
    }
}
