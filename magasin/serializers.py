"""
from rest_framework.serializers import ModelSerializer
 
from shop.models import Categorie
 
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = Categorie
        fields = ['id', 'name']
"""