from rest_framework import viewsets
from items.serializers import Item, ItemSerializer
from rest_framework import permissions, pagination, response
from datetime import datetime

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class ItemViewSet(viewsets.ModelViewSet):

    pagination_class = StandardResultsSetPagination

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    permission_classes = [
        permissions.IsAuthenticated, 
        permissions.IsAdminUser
    ]
    
    def list(self, request):
        
        isExpired = request.GET.get("expired", False)
        filterKey =  "expired_at__lt"  if isExpired else "expired_at__gte" 
        queryset  = self.get_queryset().filter(**{ filterKey: datetime.now() })
        paginate_queryset = self.paginate_queryset(queryset)
        
        serializer = self.get_serializer(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)
