from django.urls import path, include
# from django.urls.conf import include      # bir üstteki gibi de bu şekilde de include import edilecilir.
from .views import home

urlpatterns = [
    path('home/', home),
]
