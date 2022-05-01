import plotly.graph_objects as go
import yfinance as yf

tsla = yf.Ticker("TSLA")
hist = tsla.history(period='5d')
print(hist.head())

fig = go.Figure(data = go.Scatter(x=hist.index, y = hist['Close']))
fig.show()