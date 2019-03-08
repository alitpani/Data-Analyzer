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
    df = get_history(symbol=sym,start=date(int(st[:4]),int(st[5:7]),int(st[8:])),end=date(int(en[:4]),int(en[5:7]),int(en[8:])))
    trace = go.Ohlc(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])
    data = [trace]
    py.offline.plot(data, filename='simple_candlestick')
    return HttpResponse('<h1>Thank You</h1>')
