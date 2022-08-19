from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('chart/', views.post_chart, name='post_chart'),
    path('table/', views.post_table, name='post_table'),
]