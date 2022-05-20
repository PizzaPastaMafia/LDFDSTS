import java.util.ArrayList;

public class Stocks {
    private ArrayList<Stock> stocks;
    public Stocks(ArrayList<Stock> stocks) {
        this.stocks = stocks;

    }

    public void add(Stock stock) {
        this.stocks.add(stock);
    }

    public Stock getStockByTicker(String ticker) {
        for (Stock stock : stocks) {
            if (stock.getTicker().equals(ticker)) {
                return stock;
            }
        }

        return null;
    }

    public Stock getStockByName(String name){
        for (Stock stock : stocks) {
            if (stock.getName().equals(name)){
                return stock;
            }
        }

        return null;
    }
    
}
