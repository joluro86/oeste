from django.urls import path
from .views import (
    PublicadorListView,
    PublicadorDetailView,
    PublicadorCreateView,
    PublicadorUpdateView,
    PublicadorDeleteView
)

urlpatterns = [
    path('', PublicadorListView.as_view(), name='publicador_list'),
    path('<int:pk>/', PublicadorDetailView.as_view(), name='publicador_detail'),
    path('nuevo/', PublicadorCreateView.as_view(), name='publicador_create'),
    path('<int:pk>/editar/', PublicadorUpdateView.as_view(), name='publicador_update'),
    path('<int:pk>/eliminar/', PublicadorDeleteView.as_view(), name='publicador_delete'),
]

