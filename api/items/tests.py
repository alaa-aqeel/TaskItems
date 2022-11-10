from PIL import Image
from django.utils import timezone
from io  import BytesIO
from datetime import timedelta, datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils.translation import gettext as __
from items.serializers import Item, ItemSerializer
from django.contrib.auth.models import User
from rest_framework.settings import api_settings

class Fake:
    

            
    
    def fake_image_upload(self):
        byte = BytesIO()
        image = Image.new('RGB', (100, 100))
        image.save(byte, "jpeg")
        return SimpleUploadedFile("testing_image.jpg", byte.getvalue())
    
        
    def fake_expired_date(self, days=2):
        now = timezone.now()
        return str(now + timedelta(days=days))

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
        
        self.fake = Fake()

    def __create_many_items(self, count=1):
        
        for index in range(0, count):   
            Item.objects.create(**{
                "name": f"testing name {index}",
                "image": self.fake.fake_image_upload(),
                "expired_at": self.fake.fake_expired_date(2)
            })


    def test_create_new_item(self):
        
        self.client.force_authenticate(self.user)
        
        response = self.client.post(reverse("item-viewset-list"), data={
                    "name": "testing items", 
                    "image": self.fake.fake_image_upload(), 
                    "expired_at": self.fake.fake_expired_date()
                }, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    
    def test_get_items(self):
        
        self.__create_many_items(5)
        self.client.force_authenticate(self.user)
        
        response = self.client.get(reverse("item-viewset-list"))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results", [])), 5)
        
        
    def test_pagination_items(self):
        
        self.__create_many_items(15)
        self.client.force_authenticate(self.user)
        
        response_page_1 = self.client.get(reverse("item-viewset-list"), data={"page": 1})
        self.assertEqual(response_page_1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_page_1.data.get("results", [])), api_settings.PAGE_SIZE)
        
        response_page_2 = self.client.get(reverse("item-viewset-list"), data={"page": 2})
        self.assertEqual(response_page_2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_page_2.data.get("results", [])), 5)
        
        
    def test_update_item(self):
        
        self.client.force_authenticate(self.user)
         
        item = Item.objects.create(**{
            "name": f"testing name asdfasfd",
            "image": self.fake.fake_image_upload(),
            "expired_at": self.fake.fake_expired_date(2)
        })
        
        response = self.client.put(
                reverse("item-viewset-detail", kwargs={"pk": item.id}), 
                data={
                    "name": f"new testing name new",
                    "expired_at": self.fake.fake_expired_date(2),
                    "image": self.fake.fake_image_upload()
                })
        

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "new testing name new")
        
        
    def test_delete_item(self):
        
        self.client.force_authenticate(self.user)
         
        item = Item.objects.create(**{
            "name": f"testing name asdfasfd",
            "image": self.fake.fake_image_upload(),
            "expired_at": self.fake.fake_expired_date(2)
        })
        
        response = self.client.delete(reverse("item-viewset-detail", kwargs={"pk": item.id}))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)