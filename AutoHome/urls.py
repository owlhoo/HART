from django.urls import path

from . import views

app_name = 'AutoHome'

urlpatterns = [
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('status', views.StatusView.as_view(), name='status'),
    path('control', views.ControlView.as_view(), name='control'),
]
