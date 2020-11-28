from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tournaments/', include('tournament.urls')),
    path('team/', include('teams.urls')),
    path('match/', include('matchs.urls')),
    path('player/', include('players.urls')),
]
