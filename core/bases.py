from django.urls import path
from core.views import views

app_name = 'bases'

urlpatterns = [
    path('', views.index)
]