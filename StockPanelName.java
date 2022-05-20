import javax.swing.*;
import javax.swing.BoxLayout;
import java.awt.*;

public class StockPanelName extends JPanel {
    public StockPanelName(Stock stock){
        setLayout(new GridLayout(2, 2));

        add(new JLabel(stock.getName()));
        add(new JLabel(stock.getTicker()));
        add(new JLabel(Float.toString(stock.getPrice())));
        JLabel upOrDown = new JLabel(Float.toString(stock.getChange()));
        if(stock.isUp()){
            upOrDown.setForeground(Color.green);
        } else {
            upOrDown.setForeground(Color.red);
        }
        add(upOrDown);

        setVisible(true);

    }
}
