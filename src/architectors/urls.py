from django.urls import path

from architectors.views import ArchitectorAPI, ArchitectorDetailAPI

urlpatterns = [
    path('<int:architector_id>/', ArchitectorDetailAPI.as_view(), name='api-architector'),
    path('', ArchitectorAPI.as_view(), name='api-architectors'),
]
