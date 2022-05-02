//JToggeButton 
import javax.swing.*;
import java.awt.*;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;

public class JToggleButtonDemo extends JApplet implements ItemListener
{
    JLabel jlab;
    JToggleButton jtb;
    public void init()
    {
        Container cp=getContentPane();
        cp.setLayout(new FlowLayout());
        jlab=new JLabel("Button is off");
        jtb=new JToggleButton("On/Off");
        jtb.addItemListener(this);
        cp.add(jtb);
        cp.add(jlab);
    }
    public void itemStateChanged(ItemEvent ie)
    {
        if(jtb.isSelected())
        jlab.setText("Button is on");
        else
        jlab.setText("Button is off");
    }
}
