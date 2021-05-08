from django.urls import path
from  home import  views

urlpatterns = [
    path('',views.landing,name='landing-page'),
    path('about/',views.about,name='about-page'),
    path('contact/',views.contact,name='contact-page'),
    path('services/',views.services,name='services-page'),

]