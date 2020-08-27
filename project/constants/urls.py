from django.urls import path

from .views import CheckAppStatus

urlpatterns = [
    path('check-status', CheckAppStatus.as_view(), name='check-app-status')
]
