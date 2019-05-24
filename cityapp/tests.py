from django.test import TestCase
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "city.settings")
django.setup()
from cityapp.models import City

# Create your tests here.
if __name__ == '__main__':
    res = City.objects.all()
    print(res)
    # print(111)