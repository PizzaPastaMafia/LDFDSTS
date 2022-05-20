public class Stock {
    private String name;
    private String ticker;
    private float price;
    private float change;
    private double mrktcap;
    private boolean isUp;

    public Stock(String name, String ticker, float price, float change, double mrktcap, boolean isUp){
        this.name = name;
        this.ticker = ticker;
        this.price = price;
        this.change = change;
        this.mrktcap = mrktcap;
        this.isUp = isUp;
    }

    public String getName(){
        return name;        
    }

    public String getTicker(){
        return ticker;
    }

    public float getPrice(){
        return price;
    }

    public float getChange(){
        return change;
    }

    public double getMrktcap(){
        return mrktcap;
    }

    public boolean isUp(){
        return isUp;
    }

    public void setPrice(float price){
        this.price = price;
    }

    public void setChange(float change){
        this.change = change;
    }

    public void setCap (double cap){
        this.mrktcap = cap;
    }

    public void setUp(boolean isUp){
        this.isUp = isUp;
    }


    
}
