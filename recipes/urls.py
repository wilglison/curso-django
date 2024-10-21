
from django.urls import path
from recipes.views import home, sobre
    

urlpatterns = [
    path('sobre/', sobre),
    path('', home),
]
