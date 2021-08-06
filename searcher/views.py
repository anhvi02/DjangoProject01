from django.shortcuts import render
from searcher.models import Info
# Create your views here.
def home(request):
    return render(request, 'searcher/home.html')

def us(request):
    return render(request, 'searcher/us.html')

def analytics(request):
    return render(request, 'searcher/analytics.html')

def recommend(request):
    return render(request, 'searcher/recommend.html')

def result(request):
    res_sale_rate = Info.objects.order_by('sale_rate')
    sale_rate_dict = {'top_sale': res_sale_rate}
    return render(request, 'searcher/result.html', context = sale_rate_dict)
