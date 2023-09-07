from django.shortcuts import render, redirect, get_object_or_404
from .models import TradeData
from .forms import TradeDataForm
import numpy as np
import json
from django.shortcuts import render
from .models import TradeData 
import matplotlib.pyplot as plt

def index(request):

    with open('jsondata/stock_market_data.json', 'r') as json_file:
        data = json.load(json_file)

    datapoints = [{"x": entry["date"], "y": entry["close"]} for entry in data]
    datapoints2 = [{"x": entry["date"], "y": entry["volume"]} for entry in data]

    return render(request, 'myapp/home.html', {"datapoints": datapoints, "datapoints2": datapoints2})

def home(request):
    trade_data = TradeData.objects.all()
    return render(request, 'myapp/home.html', {'trade_data': trade_data})

def update(request, pk):
    trade_data = get_object_or_404(TradeData, pk=pk)
    if request.method == 'POST':
        form = TradeDataForm(request.POST, instance=trade_data)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TradeDataForm(instance=trade_data)
    return render(request, 'myapp/update.html', {'form': form, 'trade_data': trade_data})

def delete(request, pk):
    trade_data = get_object_or_404(TradeData, pk=pk)
    if request.method == 'POST':
        trade_data.delete()
        return redirect('home')
    return render(request, 'myapp/delete.html', {'trade_data': trade_data})