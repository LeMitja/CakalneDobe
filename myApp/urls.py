from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("databasetest/", views.databasetest, name="CakDobe"),
    path("get-chart-data/", views.get_chart_data, name="get_chart_data"),
    path('search-vzs', views.search_vzs, name='search-vzs'),
]