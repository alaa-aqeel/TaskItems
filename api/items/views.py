from rest_framework import viewsets
from django.utils import timezone
from items.serializers import Item, ItemSerializer
from rest_framework import permissions, response



class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    paginate_by = 10 
    permission_classes = [
        permissions.IsAuthenticated, 
        permissions.IsAdminUser
    ]
    
    
    def list(self, request):
        print(timezone.now().date())
        isExpired = request.GET.get("expired", False)
        filterKey =  "expired_at__lt"  if isExpired else "expired_at__gte" 
        queryset  = self.get_queryset()
        
        page_queryset = self.paginate_queryset(queryset)

        if page_queryset is not None:
            serializer = self.get_serializer(page_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset,  many=True)
        return response.Response(serializer.data)