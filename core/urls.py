from django.urls import path

from .views import index, galeria, logout, login, restrito, galeriarestrita

urlpatterns = [
    path('', index, name='index'),
    path('galeria/<str:pk>', galeria, name='galeria'),
    path('galeria-restrita/<str:pk>', galeriarestrita, name='galeria-restrita'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('restrito/', restrito, name='restrito'),
]
