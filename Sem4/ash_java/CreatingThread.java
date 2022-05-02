class A extends Thread
{
    public void run()
    {
        for(int i=0;i<=5;i++)
        {
            System.out.println("From thread A: "+i);
        }
        System.out.println("Exit from A");
    }
}
class B extends Thread
{
    public void run()
    {
        for(int j=0;j<5;j++)
        {
            System.out.println("From thread B: "+j);
        }
        System.out.println("Exit from B");
    }
}
class C extends Thread
{
    public void run()
    {
        for(int k=0;k<5;k++)
        {
            System.out.println("From thread C: "+k);
        }
        System.out.println("Exit from C");
    }
}
public class CreatingThread {
    public static void main(String args[])
    {
        new A().start();
        new B().start();
        new C().start();    
    }
}
