import tkinter as tk
import matplotlib.pyplot as plt
import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.rowconfigure(0, minsize=500)    # minimal height
window.columnconfigure(0, minsize=700) # minimal width

class Stock:
    def __init__(self, ticker, p):
        self.stock_name = ticker
        self.period = p
        self.stock_data = yf.Ticker(ticker)
        self.hist = self.stock_data.history(period=self.period)
        self.title = self.stock_name

    def getX(self):
        x=self.hist.index
        return x

    def getY(self):
        y = self.hist['Close']
        return y

    def getTitle(self):
        return self.title

    def plotGraph(self):
        fig, ax = plt.subplots(1)
        ax.plot(self.getX(), self.getY())
        ax.set_title(self.getTitle())
        fig.show()
        
        return fig

    def showGraph(self):
        dataPlot = FigureCanvasTkAgg(self.plotGraph(), master=window)
        dataPlot.draw()
        dataPlot.get_tk_widget().grid(row=0, column=0)

stock = Stock("fb", "1y")
stock.showGraph()


window.mainloop()