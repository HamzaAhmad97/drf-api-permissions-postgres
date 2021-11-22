from rest_framework import generics
from rest_framework.response import Response

from .serializers import MammalSerializer
from .models import Mammal

class MammalList(generics.ListCreateAPIView):
    queryset = Mammal.objects.all()
    serializer_class = MammalSerializer


class MammalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mammal.objects.all()
    serializer_class = MammalSerializer 
