from django.urls import path
from .views import MammalDetail, MammalList

urlpatterns = [
    path('',MammalList.as_view(), name='mammal_list'),
    path('<int:pk>/', MammalDetail.as_view(), name='mammal_detail')
]