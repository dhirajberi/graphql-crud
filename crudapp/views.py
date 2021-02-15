from django.shortcuts import render
from .models import Test

# Create your views here.
def home(request):
    tests = Test.objects.all()
    return render(request, 'index.htm', {'tests':tests})