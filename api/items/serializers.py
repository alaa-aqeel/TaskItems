from rest_framework import serializers
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    
    image = serializers.ImageField(required=False)
    expired_at = serializers.DateTimeField(format="%Y-%m-%d")
    
    
    class Meta:
        model = Item
        
        
        fields = [
            'id', 
            'name', 
            'image', 
            'expired_at', 
            'created_at', 
            'updated_at'
        ]
        
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
        
        
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ItemSerializer, self).__init__(*args, **kwargs)
        