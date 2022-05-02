//JList 

import javax.swing.*;
import java.awt.*;
import javax.swing.event.*;

public class JListDemo extends JFrame implements ListSelectionListener
{
    JList colors;
    Container c;
    public JListDemo()
    {
        c=getContentPane();
        c.setLayout(new FlowLayout());
        String names[]={"Red","Green","Blue","Cyan","Yellow","Magenta"};
        colors = new JList(names);
        colors.setVisibleRowCount(5);
        colors.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        c.add(new JScrollPane(colors));
        colors.addListSelectionListener(this);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setTitle("Practicing JList");
        setSize(300,300);
        setVisible(true);
    }
    public void valueChanged(ListSelectionEvent e)
    {
        String str=(String)colors.getSelectedValue();
        if (str.equals("Red"))
        c.setBackground(Color.red);
        else if (str.equals("Green"))
        c.setBackground(Color.green);
        else if (str.equals("Blue"))
        c.setBackground(Color.blue);
        else if (str.equals("Cyan"))
        c.setBackground(Color.cyan);
        else if (str.equals("Yellow"))
        c.setBackground(Color.yellow);
        else if (str.equals("Magenta"))
        c.setBackground(Color.magenta);
    }
    public static void main(String args[])
    {
     new JListDemo();   
    }
}