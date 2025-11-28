from django.urls import path
from .views import MusiqueListView, MusiqueDetailView, MusiqueCreateView, MusiqueUpdateView, MusiqueDeleteView

urlpatterns = [
    path('', MusiqueListView.as_view(), name='musique_list'),
    path('musique/<int:pk>/', MusiqueDetailView.as_view(), name='musique_detail'),
    path('musique/add/', MusiqueCreateView.as_view(), name='musique_add'),
    path('musique/<int:pk>/edit/', MusiqueUpdateView.as_view(), name='musique_edit'),
    path('musique/<int:pk>/delete/', MusiqueDeleteView.as_view(), name='musique_delete'),
]
