from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import MammalSerializer
from .models import Mammal
from .permissions import IsOwnerOrReadOnly,  IsAuthorOrReadOnly

class MammalList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Mammal.objects.all()
    serializer_class = MammalSerializer


class MammalDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,IsOwnerOrReadOnly,IsAuthenticated)
    queryset = Mammal.objects.all()
    serializer_class = MammalSerializer 
