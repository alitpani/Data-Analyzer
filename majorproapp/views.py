from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def plot(request):
    start_date1=request.GET['start_date']
    end_date1=request.GET['end_date']
    symbol1=request.GET['symbol']

    return HttpResponse(symbol1)
