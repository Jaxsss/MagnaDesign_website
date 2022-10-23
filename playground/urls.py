from django.urls import path
from . import views
#sd
urlpatterns = [
    path('uvod', views.get_uvod, name='uvod'),
    path('kontakt', views.get_kontakt, name='kontakt'),
    path('projekt_logotvorba_vaclavovice', views.get_projekt_logotvorba_vaclavovice, name='projekt-logotvorba-vaclavovice'),
]