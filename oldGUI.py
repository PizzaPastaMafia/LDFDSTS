import tkinter as tk
import matplotlib.pyplot as plt
import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.rowconfigure(0, minsize=500)    # minimal height
window.columnconfigure(0, minsize=700) # minimal width

tsla = yf.Ticker("TSLA")
hist = tsla.history(period='5y')

x=hist.index
y = hist['Close']

fig = plt.plot_sheet(x, y)
fig.show()

window.mainloop()