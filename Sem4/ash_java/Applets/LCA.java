//Program for Life Cycle of an applet


import java.awt.*;
import java.applet.*;

public class LCA extends Applet
{
    String msg1,msg2,msg3,msg4;
    public void init()
    {
        setBackground(Color.green);
        setForeground(Color.red);
        msg1="This is init()-->";
        System.out.println(msg1);
    }
    public void start()
    {
        msg2="This is start()-->";
        System.out.println(msg2);
    }
    public void stop()
    {
        msg3="This is stop()-->";
        System.out.println(msg3);
    }
    public void destroy()
    {
        msg4="This is destroy()-->";
        System.out.println(msg4);
    }
    public void paint(Graphics g)
    {
        g.drawString("Demo for basic methods of applet",10,20);
        if (msg1 != null)
        g.drawString(msg1,10,40);
        if (msg2 != null)
        g.drawString(msg2,10,60);
        if (msg3 != null)
        g.drawString(msg3,10,80);
        if (msg4 != null)
        g.drawString(msg4,10,100);
    }
}