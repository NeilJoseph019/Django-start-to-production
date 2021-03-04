from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="inputPage"),
    path('details/',views.display, name="outputPage")
]