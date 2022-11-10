from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from api.serializers import UserSerializer
from rest_framework import permissions

class UserProfileAPI(APIView):
    
    permission_classes = [
        permissions.IsAuthenticated, 
        permissions.IsAdminUser
    ]
    
    def get(self, request):
        
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
