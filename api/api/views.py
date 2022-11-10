from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from api.serializers import ProfileSerializer


class ProfileAPI(generics.UpdateAPIView):
    
    
    def get(self, request, *args, **kwargs):
        
        profile_serializer = ProfileSerializer(request.user)
        return Response(profile_serializer.data)
    
