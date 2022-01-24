//Fibbonacci seriesw
public class fibonacci {
    public static void main(String args[])
    {
        int i=0,a=0,b=1,c=0,k=5;
        System.out.println(a);
        System.out.println(b);
        while(i<k)
        {
            c=a+b;
            System.out.println(c);
            a=b;
            b=c;
            i++;
        }        

    }
}
