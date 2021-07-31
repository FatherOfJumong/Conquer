from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
 


def home_page(request):
    return render(request,'firstApp/home.html')


def contact_page(request):
    return render(request,'firstApp/contact.html')





def test(request):
    return render(request,'firstApp/test.html')


def corona(request):
    return render(request,'firstApp/folium_folder/CoronaMap.html')







def courses(request):
    return render(request,'firstApp/courses.html')


def pythonbasics(request):
    return render(request,'firstApp/courses/pythonbasics.html')

