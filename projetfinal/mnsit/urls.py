from django.urls import path
from .views import PredictDigit

urlpatterns = [
    path("predict_digit/", PredictDigit.as_view(), name="predict_digit"),
]
