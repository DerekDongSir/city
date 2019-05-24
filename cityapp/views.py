from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from cityapp.models import City
# Create your views here.
def index(request):
    provinces = City.objects.filter(type=1)
    return render(request,'city.html',{'province':provinces})


def get_city(request):
    pro_id = int(request.GET.get('pro_id'))
    cities = list(City.objects.filter(pid=pro_id))
    def my_default(city):
        if isinstance(city,City):
            return {'id':city.id,'cityname':city.cityname}
    return JsonResponse(cities,safe=False,json_dumps_params={'default':my_default})


def get_town(request):
    city_id = int(request.GET.get('city_id'))
    towns = list(City.objects.filter(pid=city_id))
    def my_default(town):
        if isinstance(town,City):
            return {'id':town.id,'townname':town.cityname}
    return JsonResponse(towns,safe=False,json_dumps_params={'default':my_default})
