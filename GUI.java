import javax.swing.JFrame;
import javax.swing.*;
import javax.swing.BoxLayout;
import java.awt.*;
import java.awt.event.*;
import java.io.IOException;  

public class GUI extends JFrame implements MouseListener {
    private Stock stock;
    public GUI(Stock stock) {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1000,600);
        setTitle("Lorenzo Del Forno Dynamic Stock Trading Simulator");
        MouseListener mouseListener;
        JButton GS = new JButton("get stock");
        //GS.addMouseListener(this);
        //add(GS);
        try {
            add(new StockPanelMain(stock));
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        setVisible(true);
    }        

    public void setStock(Stock stock) {
        this.stock = stock;
    }

    @Override
    public void mouseClicked(MouseEvent arg0) {
        this.removeAll();
        
    }

    @Override
    public void mouseEntered(MouseEvent arg0) {
        // TODO Auto-generated method stub
        
    }

    @Override
    public void mouseExited(MouseEvent arg0) {
        // TODO Auto-generated method stub
        
    }

    @Override
    public void mousePressed(MouseEvent arg0) {
        // TODO Auto-generated method stub
        
    }

    @Override
    public void mouseReleased(MouseEvent arg0) {
        // TODO Auto-generated method stub
        
    }
}
