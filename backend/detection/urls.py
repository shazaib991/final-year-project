from django.urls import path
from .views import FractureDetectionView

urlpatterns = [
    path('predict/', FractureDetectionView.as_view(), name='predict'),
]
