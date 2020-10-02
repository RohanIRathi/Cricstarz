from django.urls import path
from . import views

app_name="teams"
urlpatterns = [
    path('<int:tournamentid>/new/', views.TeamCreateView.as_view(), name="addteam"),
]