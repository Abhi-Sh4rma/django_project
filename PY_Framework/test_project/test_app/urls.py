from django.urls import path
from .views import index

urlpatterns = [
    path('', index)  # Map the root URL to the index view
]
