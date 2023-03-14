import yfinance as yf
import plotly.graph_objects as go
import kaleido
import plotly.offline as pyo


def get_graph(comp: str, per="1y"):
    print(comp, per)
    company = yf.Ticker(comp)
    hist = company.history(period=per)
    hist.head()
    fig = go.Figure(data=go.Scatter(x=hist.index, y=hist['Close']))
    fig.update_layout(xaxis_title= "date", yaxis_title="price($)", title = f"{comp} stock prices")
    print(fr"C:\Cyber_Stock_project\Bot_code\Test_pictures\{comp}.png")
    fig.write_image(fr"C:\Cyber_Stock_project\Bot_code\Test_pictures\{comp}.png")


def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]