from django.shortcuts import render
from .models import Weather, City
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime

# Create your views here.
def post_list(request):
    return render(request, 'weater/index.html',{})

def post_chart(request):
    labels = []
    data_chart = []

    if request.method == 'GET':
        city_form = request.GET.get('city', False)
        data_form = request.GET.get('data_form', False)

        queryset = Weather.objects.filter(city_name_weather__city_name=city_form)
        for info in queryset:
            labels.append(info.time)
            data_chart.append(info.temperature)

    return render(request, 'weater/chart.html', {'labels': labels, 'data': data_chart})



def post_table(request):
    my_weth = Weather.objects.all()
    my_city = City.objects.all()
    paginator = Paginator(my_weth, 4)
    page_number = request.GET.get('page')  # GET параметр page
    page_obj = paginator.get_page(page_number)

    return render(request, 'weater/table.html',{'my_weth': my_weth,'my_city': my_city,'page_obj': page_obj})
