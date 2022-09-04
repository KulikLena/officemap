from django.contrib import admin
from django.urls import path
from officesrates import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.OfficeList.as_view()),
    path('map_density/', views.offices_map_density),
]



