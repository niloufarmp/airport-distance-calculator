from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from airport import views

urlpatterns = [
    url('admin/', admin.site.urls),
    path('api/airport/<str:first>/<str:second>/distance', views.DistanceComputeView.as_view()),
    path('api/airport/list', views.ListAirportsView.as_view())
]
