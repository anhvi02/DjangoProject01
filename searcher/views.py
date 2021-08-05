from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'searcher/home.html')

def us(request):
    return render(request, 'searcher/us.html')

def analytics(request):
    return render(request, 'searcher/analytics.html')

def result(request):
    context = []
    return
