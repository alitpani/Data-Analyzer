from django.shortcuts import render
from django.http import HttpResponse
import plotly as py
import plotly.graph_objs as go
from datetime import date
from nsepy import get_history
import pandas as pd
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')
def plot(request):
    st=request.POST['name']
    en=request.POST['email']
    sym=request.POST['service']
    chart=request.POST['plot']
    df = get_history(symbol=sym,start=date(int(st[:4]),int(st[5:7]),int(st[8:])),end=date(int(en[:4]),int(en[5:7]),int(en[8:])))
    if chart=='Candel Chart':
        
        trace = go.Ohlc(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])
        data = [trace]
        layout = {'title': sym+' Plot','yaxis': {'title': sym},}
        fig = dict(data=data, layout=layout)
        py.offline.plot(fig, filename='simple_candlestick')
    elif chart=='Time Series':
        trace_low = go.Scatter(
                x=df.index,
                y=df['Trades'],
                name = "Trades",
                line = dict(color = '#7F7F7F'),
                opacity = 0.8)

        data = [trace_low]
        layout = dict(title = sym+' Trade')


        fig = dict(data=data, layout=layout)
        py.offline.plot(fig, filename='simple_candlestick')
        

    return HttpResponse('<h1>Thank You</h1>')
