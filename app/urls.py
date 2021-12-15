from django.urls import path
from . views import fibonacci_calculate_view

urlpatterns = [
    path('', fibonacci_calculate_view),
]
