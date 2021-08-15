from .models import Memant
from rest_framework import serializers


class MemantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memant
     # if you want only specific fields
     #   fields = ['heiza', 'heiza_text', 'heiza_answer', 'id']
        # if you want all fields
        fields = '__all__'
