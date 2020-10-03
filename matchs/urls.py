from django.urls import path
from . import views

app_name = 'match'
urlpatterns = [
    path('<int:tournamentid>/new/', views.MatchCreateView.as_view(), name="addmatch"),
]