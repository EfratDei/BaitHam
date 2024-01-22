from django.urls import path
from .views import all_articles


app_name = 'Article'

urlpatterns = [
    path('articles/', all_articles, name='articles'),
]