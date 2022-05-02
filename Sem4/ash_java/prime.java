public class prime {
    public static void main(String args[])
    {
        int i,in=14,a=0;
        for(i=2;i<in;i++)
        {
            if (in%i==0){
                a++;
                break;
            }
        }
        if (a == 0){
            System.out.println(in+" is prime");

        }
        else{
            System.out.println(in+" is not prime");
        }
    }
}