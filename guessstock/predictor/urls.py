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
