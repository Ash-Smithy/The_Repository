
/*
Constructors :
1.) It's a special method with the same name 
as that of its class and odes not have any return 
type, not even void
2.)It initialises the instance variables 
3.)It gets called when the object is created 
   implicitly
*/
class Rectangle
{
    int l,b;
    Rectangle(int x,int y)
    {
        l = x;
        b = y; 
    }
    int rectarea()
    {
        int area = l*b;
        return area;
    }
}
public class constructors{
    public static void main(String args[])
    {
        Rectangle c1 = new Rectangle(10,5);
        //this statement creates object c1 and 
        //implicitly calls the constructor and passes 
        //10 and 5 which are initialized to x and y
        Rectangle c2 = new Rectangle(12,6);
        int a1=c1.rectarea();
        int a2=c2.rectarea();
        System.out.println("area 1 : "+a1);
        System.out.println("area 2 : "+a2);
    }
}