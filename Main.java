import java.io.IOException;

class Main {
    public static void main(String[] args){
        Stock apple = new Stock("Apple", "AAPL", (float)975, (float)9, (double)10000, true);
        
        Stock meta = new Stock("Meta", "FB", (float)234, (float)2, (double)10000, false);

        
        try {
            Process process = Runtime.getRuntime().exec("./newGUI.py " + apple.getTicker() + " 1y");
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }


        GUI gui = new GUI(apple);

        gui.setStock(meta);

    }
}