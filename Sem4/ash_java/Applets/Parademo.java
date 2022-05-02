// Parameters to applet
import java.awt.*;
import java.applet.*;

public class Parademo extends Applet
{
    int a,b;
    public void init()
    {
        a=Integer.parseInt(getParameter("first"));
        b=Integer.parseInt(getParameter("second"));
    }
    public void paint(Graphics g)
    {
        g.drawString("Addition: "+(a+b),10,20);
        g.drawString("Subtraction: "+(a-b),10,40);
        g.drawString("Multiplication: "+(a*b),10,60);
        g.drawString("Division: "+(a/b),10,80);
        g.drawString("Mod: "+(a%b),10,100);
    }
}