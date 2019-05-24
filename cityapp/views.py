from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from cityapp.models import City
# Create your views here.
def index(request):
    provinces = City.objects.filter(type=1)
    return render(request,'city.html',{'province':provinces})


def get_city(request):
    pro_id = int(request.GET.get('pro_id'))
    print(pro_id)
    cities = City.objects.filter(pid=pro_id)
    return JsonResponse(pro_id,safe=False)


def get_town(request):
    city_id = request.GET.get('city_id')
    towns = City.objects.filter(pid=city_id)