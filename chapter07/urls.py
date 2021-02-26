from django.urls import path
from . import views

app_name = "chapter07"

urlpatterns = [
    path('work01/', views.work01, name="work01"),
    path('work02/', views.work02, name="work02"),
    path('work03/', views.work03, name="work03"),
    path('work04/', views.work04, name="work04"),
]
