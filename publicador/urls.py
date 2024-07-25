from django.contrib import admin
from django.urls import path
from publicador.views import publicador_detail, crear_publicador
urlpatterns = [
    path('/<int:pk>/', publicador_detail, name='publicador_detail'),
    path('/nuevo/', crear_publicador, name='crear_publicador'),

]
