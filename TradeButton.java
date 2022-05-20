import javax.swing.*;
import javax.swing.BoxLayout;
import java.awt.*;


public class TradeButton extends JPanel {
    public TradeButton(){
        setLayout(new GridLayout(2, 1));
        JTextField tradeLabel = new JTextField("0");
        add(tradeLabel);

        JPanel tradePanel = new JPanel();
        tradePanel.setLayout(new FlowLayout());
        tradePanel.add(new JButton("sell"));
        tradePanel.add(new JButton("buy"));

        add(tradePanel);

        setVisible(true);
    }
}
