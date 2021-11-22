from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import MammalSerializer
from .models import Mammal
from .permissions import IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly

class MammalList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Mammal.objects.all()
    serializer_class = MammalSerializer


class MammalDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,IsAuthenticatedOrReadOnly)
    queryset = Mammal.objects.all()
    serializer_class = MammalSerializer 
