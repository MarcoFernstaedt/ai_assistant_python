from django.urls import path
from .views import get_gpt_response

urlpatterns = [
    path('gpt/', get_gpt_response, name='gpt'),
]