from django.urls import path, include

urlpatterns = [
    path('constants/', include('project.constants.urls'))
]
