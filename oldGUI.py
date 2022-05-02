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

fig, ax = plt.subplots(1)
ax.plot(x, y)
fig.show()

dataPlot = FigureCanvasTkAgg(fig, master=window)

dataPlot.draw()
dataPlot.get_tk_widget().grid(row=0, column=0)

window.mainloop()