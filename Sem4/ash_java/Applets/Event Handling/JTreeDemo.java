//Program to implement Jtree

import java.awt.*;
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.tree.*;

public class JTreeDemo extends JApplet implements TreeSelectionListener
{
    JTree tree;
    JLabel jlab;
    public void init()
    {
        Container cp=getContentPane();
        cp.setLayout(new FlowLayout());
        DefaultMutableTreeNode top= new DefaultMutableTreeNode("options");
        DefaultMutableTreeNode a = new DefaultMutableTreeNode("A");
        top.add(a);
        DefaultMutableTreeNode a1= new DefaultMutableTreeNode("A1");
        a.add(a1);
        DefaultMutableTreeNode a2= new DefaultMutableTreeNode("A2");
        a.add(a2);
        DefaultMutableTreeNode b= new DefaultMutableTreeNode("B");
        top.add(b);
        DefaultMutableTreeNode b1= new DefaultMutableTreeNode("B1");
        b.add(b1);
        DefaultMutableTreeNode b2= new DefaultMutableTreeNode("B2");
        b.add(b2);
        DefaultMutableTreeNode b3= new DefaultMutableTreeNode("B3");
        b.add(b3);
        tree=new JTree(top);
        JScrollPane jsp = new JScrollPane(tree);
        cp.add(jsp);
        jlab = new JLabel();
        add(jlab, BorderLayout.SOUTH);
        tree.addTreeSelectionListener(this);
    }
    public void valueChanged(TreeSelectionEvent tse)
    {
        jlab.setText("Selection is: "+tse.getPath());
    }
}
