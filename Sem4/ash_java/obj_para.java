class Test
{
    int a,b;
    Test(int i,int j)
    {
        a=i;
        b=j;
    }
    boolean equals(Test t)
    {
        if(t.a==a && t.b==b)
        return true;
        else 
        return false;
    }
}
public class obj_para {
    public static void main(String args[])
    {
        Test b1=new Test(10,20);
        Test b2=new Test(10,20);
        Test b3=new Test(10,10);
        System.out.println(b1.equals(b2));
        System.out.println(b2.equals(b3));
    }
    
}
