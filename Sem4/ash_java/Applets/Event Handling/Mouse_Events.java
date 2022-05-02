import java.awt.*;
import java.awt.event.*;
import java.applet.*;

public class Mouse_Events extends Applet implements MouseListener, MouseMotionListener
{
    String msg;
    public void init()
    {
        msg="";
        addMouseListener(this);
        addMouseMotionListener(this);
    }
    public void mouseClicked(MouseEvent e)
    {
        msg="Mouse Clicked";
        repaint();
    }
    public void mouseEntered(MouseEvent e)
    {
        msg="Mouse Entered";
        repaint();
    }
    public void mouseExited(MouseEvent e)
    {
        msg="Mouse Exited";
        repaint();
    }
    public void mousePressed(MouseEvent e)
    {
        msg="Mouse Pressed";
        repaint();
    }
    public void mouseDragged(MouseEvent e)
    {
        msg="Mouse Dragged";
        repaint();
    }
    public void mouseReleased(MouseEvent e)
    {
        msg="Mouse Released";
        repaint();
    }
    public void mouseMoved(MouseEvent e)
    {
        msg="Mouse Moved";
        repaint();
    }
    public void paint(Graphics g)
    {
        g.drawString(msg,20,20);
    }
}
