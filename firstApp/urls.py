from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('contact',views.contact_page, name='contact-page'),
    path('test',views.test, name='test'),
    path('covidstats',views.corona,name='covid19'),
    path('courses/',views.courses,name = 'courses'),
    path('pythonbasics/',views.pythonbasics, name='pythonbasics'),
]