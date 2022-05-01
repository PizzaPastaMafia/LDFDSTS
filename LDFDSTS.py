import plotly.graph_objects as go
import yfinance as yf
import matplotlib.pyplot as plt

tsla = yf.Ticker("TSLA")
hist = tsla.history(period='5y')
print(hist.head())

#fig = go.Figure(data = go.Scatter(x=hist.index, y = hist['Close']))
#fig.show()

x=hist.index
y = hist['Close']

plt.plot(x, y)
plt.show()