from PIL import Image
from io  import BytesIO
from datetime import datetime, timedelta
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils.translation import gettext as __
from items.serializers import Item, ItemSerializer
from django.contrib.auth.models import User

class ItemTests(APITestCase):
    
    def setUp(self):
        
        self.user = User.objects.create_user(**{
            "username": "test_super_admin",
            "email": "test@email.com",
            "password": "12345678",
            "is_superuser": True,
            "is_active": True,
            "is_staff": True
        })

    
    def __fake_image_upload(self):
        byte = BytesIO()
        image = Image.new('RGB', (100, 100))
        image.save(byte, "jpeg")
        return SimpleUploadedFile("testing_image.jpg", byte.getvalue())
        
    def __fake_expired_date(self, days=3):
        
        return str(datetime.today() + timedelta(days=days))


    def test_create_new_item(self):
        
        self.client.force_authenticate(self.user)
        
        response = self.client.post(reverse("item-viewset-list"), data={
                    "name": "testing items", 
                    "image": self.__fake_image_upload(), 
                    "expired_at": self.__fake_expired_date()
                }, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
        
