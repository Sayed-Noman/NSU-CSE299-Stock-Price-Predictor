"""guessstock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from  predictor import  views

urlpatterns = [
    path('guess-stock/',views.guess_stock,name='guess_stock'),
    path('amazon-predict/',views.amazon_prediction,name='amazon_predict'),
    path('facebook-predict/',views.facebook_prediction,name='facebook_predict'),
    path('tesla-predict/',views.tesla_prediction,name='tesla_predict'),
    path('google-predict/',views.google_prediction,name='google_predict'),
    path('microsoft-predict/',views.microsoft_prediction,name='microsoft_predict'),
    path('apple-predict/',views.apple_prediction,name='apple_predict'),
    path('csv-to-graph/',views.csv_to_graph,name='csv_to_graph'),
]
