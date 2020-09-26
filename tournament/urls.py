from django.urls import path
from . import views

app_name='tournaments'
urlpatterns = [
    path('all/', views.TournamentListView.as_view(), name='all'),
    path('create/', views.TournamentCreateView.as_view(), name='create'),
]