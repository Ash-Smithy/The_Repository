package java_d3v;

class classname 
{
    int x=10,y=20;
    void putdata()
    {
        System.out.println("x = "+x);
        System.out.println("y = "+y);
    }
}
class Rectangle
{
    int length,width;
    void getdata(int x,int y)
    {
        length = x;
        width = y;
    }
    int rectArea()
    {
        int area = length*width;
        return area;   
    }
}
public class another_sample
{
    public static void main(String args[])
    {
        classname obj1 = new classname();//creating object of class and allocating memory 
        obj1.putdata();//calls the method for obj1 object

        Rectangle r1 = new Rectangle();
        r1.getdata(10,5); //calls getdata and pases x,y values
        int area = r1.rectArea(); //calls rectArea and returns area
        System.out.println("Area of rectangle is : "+area);
        Rectangle r2 = new Rectangle();
        r2.getdata(15,5);
        int area2 = r2.rectArea();
        System.out.println("Area of rectangle is : "+area2);
    
    }
}
