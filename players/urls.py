from django.urls import path
from . import views

app_name = 'players'
urlpatterns = [
    path('<int:tournamentid>/new/', views.PlayerCreateView.as_view(), name = "addplayer"),
]