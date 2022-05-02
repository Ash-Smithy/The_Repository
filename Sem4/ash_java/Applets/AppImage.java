//Program to add an image onto the applet
import java.awt.*;
import java.applet.*;
public class AppImage extends Applet
{
    Image i;
    public void start()
    {
        setBackground(Color.lightGray);
        i = getImage(getDocumentBase(),"glasses.png");
    }
    public void paint(Graphics g)
    {
        g.drawImage(i,0,0,this);
    }
}
