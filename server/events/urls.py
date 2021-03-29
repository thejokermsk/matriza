from django.urls import path
from .views import *

urlpatterns = [
  path('', EventListAPIView.as_view()),
  path('detail/<int:pk>', DetailListAPIView.as_view())
]
