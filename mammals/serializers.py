from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Mammal

class MammalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mammal
        fields = ('__all__')