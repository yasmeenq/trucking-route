from django.urls import path
from api.views import RouteAPI

urlpatterns = [
    path('route/', RouteAPI.as_view(), name='route_api'),
]
