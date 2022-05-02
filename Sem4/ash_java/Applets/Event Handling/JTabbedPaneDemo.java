//JTabbed Pane program

import javax.swing.*;
import java.awt.*;

public class JTabbedPaneDemo extends JApplet
{
    public void init()
    {
        Container cp=getContentPane();
        cp.setLayout(new FlowLayout());
        JTabbedPane jtp =new JTabbedPane();
        jtp.addTab("cities", new CitiesPanel());
        jtp.addTab("colors", new ColorsPanel());
        jtp.addTab("Flavors", new FlavorsPanel());
        add(jtp);
    }
}
class CitiesPanel extends JPanel
{
    public CitiesPanel()
    {
        JButton b1=new JButton("New York");
        add(b1);
        JButton b2=new JButton("Lodon");
        add(b2);
        JButton b3=new JButton("Hong Kong");
        add(b3);
        JButton b4=new JButton("Tokyo");
        add(b4);
    }
}
class ColorsPanel extends JPanel
{
    public ColorsPanel()
    {
        JCheckBox cb1=new JCheckBox("Red");
        add(cb1);
        JCheckBox cb2=new JCheckBox("Blue");
        add(cb2);
        JCheckBox cb3=new JCheckBox("White");
        add(cb3);
    }
}
class FlavorsPanel extends JPanel
{
    public FlavorsPanel()
    {
        JComboBox jcb=new JComboBox<>();
        jcb.addItem("Vanilla");
        jcb.addItem("Choclate");
        jcb.addItem("Strawberry");
        add(jcb);
    }
}