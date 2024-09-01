from rest_framework import serializers
from .models import Gene

class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ['id', 'title', 'content', 'author', 'created_at']