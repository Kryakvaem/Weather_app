from django.shortcuts import render
from .models import Weather, City
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def post_list(request):
    return render(request, 'weater/index.html', {})

def post_chart(request):
    my_weth = Weather.objects.all()
    return render(request, 'weater/chart.html', {'my_weth': my_weth})

def post_table(request):
    my_weth = Weather.objects.all()
    my_city = City.objects.all()
    paginator = Paginator(my_weth, 4)
    page_number = request.GET.get('page')  # GET параметр page
    page_obj = paginator.get_page(page_number)

    return render(request, 'weater/table.html',{'my_weth': my_weth,'my_city': my_city,'page_obj': page_obj})
