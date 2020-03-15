from django.urls import path
from .views import home_view,list_view,engine

urlpatterns = [
    path('', home_view, name = 'home'),
    path('list', list_view, name = 'list'),
    path('engine', engine, name = 'engine'),

]
