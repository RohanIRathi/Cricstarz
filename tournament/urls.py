from django.urls import path, include
from . import views

app_name='tournaments'
urlpatterns = [
    path('all/', views.TournamentListView.as_view(), name='all'),
    path('create/', views.TournamentCreateView.as_view(), name='create'),
    path('view/<int:pk>/', views.TournamentDetailView.as_view(), name='detail'),
]