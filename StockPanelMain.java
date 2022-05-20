import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;


public class StockPanelMain extends JPanel{
    public StockPanelMain(Stock stock) throws IOException{
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        //setSize(400,400);
        
        add(new StockPanelName(stock));

        BufferedImage bufferedImage = ImageIO.read(new File("stock_plot.png"));
        Image image = bufferedImage.getScaledInstance(640, 480, Image.SCALE_DEFAULT);
        ImageIcon icon = new ImageIcon(image);
        JLabel jLabel = new JLabel();
        jLabel.setIcon(icon);
        add(jLabel);
        
        add(new TradeButton());

        

        setVisible(true);

    }
}