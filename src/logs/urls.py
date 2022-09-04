from django.urls import path

from .views import redirect2kibana

urlpatterns = [
    path('', redirect2kibana)
]
