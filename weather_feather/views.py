from django.shortcuts import render

def index(request):
    """WeatherFeather's landing page"""
    return render(request, 'base.html')
