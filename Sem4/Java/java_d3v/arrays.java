package java_d3v;
/*
Arrays

this keyword
    this keyword is like self in python
    represents the current instance/object

access specifiers 
    public, private, protected, default
*/
class classname{
    private int len=10,wid=20;
    classname(int len,int wid)
    {
        this.len = len;
        this.wid = wid;
    }
    void method1()
    {
        System.out.println("len is : "+this.len);
        System.out.println("wid is : "+this.wid);
    }
}
public class arrays
{
    public static void main(String args[])
    {
        int a[] = new int[10]; //creating an array
        //range for the array would be 0-9 (in general it is 0-(n-1))
        //returntype arrayname[]=new returntype[array size];
        System.out.println("The array is : ");
        for(int i = 0;i<10;i++)
        {
            a[i]=i;
        }
        for(int j = 0;j<10;j++)
        {
            System.out.println(a[j]);
        }
        int twoD[][] = new int[4][5];
        //two dimensional array creating
        //returntype arrayname[][] = new returntype[r][c];
        /*
        An array is implemented as an object
        It has a special attribute "length" instance variable
        Example as follows : 
        */
        int a1[] = new int[10];
        int a2[] = {3,5,7,9,11,13,15,17};
        int a3[] = {4,3,2,1};
        System.out.println("Length of a1 is : "+a1.length);
        System.out.println("Length of a2 is : "+a2.length);
        System.out.println("Length of a3 is : "+a3.length);

        classname c1 = new classname(2,3);//calls constructor
        c1.method1();

    }
}