import os.path
import shutil
from urllib import request

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase

from backend.settings import STATIC_ROOT
from .models import Record
from .tasks import compress


class ContentTests(APITestCase):

    def setUp(self) -> None:
        # Copy the test image to correct path
        os.makedirs(os.path.join(STATIC_ROOT, "images/"), exist_ok=True)
        shutil.copyfile("test.jpg", os.path.join(STATIC_ROOT, "images/test.jpg"))

        # Create a record to test upon
        file = SimpleUploadedFile("test.jpg", open(os.path.join(STATIC_ROOT, "images/test.jpg"), "rb").read(), "image/jpeg")

        payload = {
            "name_of_fish": "MyTuna",
            "weight": "1.5",
            "length": "1.5",
            "species": "Tuna",
            "latitude": "1.5",
            "longitude": "1.5",
            "photo": file
        }

        Record.objects.create(**payload)

    def test_post_record(self):
        file = SimpleUploadedFile("test.jpg", open("test.jpg", "rb").read(), "image/jpeg")
        payload = {
            "name_of_fish": "MyTuna",
            "weight": "1.5",
            "length": "1.5",
            "species": "Tuna",
            "latitude": "1.5",
            "longitude": "1.5",
            "photo": file
        }
        url = "/records/"
        response = self.client.post(url, payload, format="multipart")
        self.assertEqual(response.status_code, 201)

    def test_list_records(self):
        url = "/records/"
        response = self.client.get(url)
        # print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_record(self):
        url = "/records/{}/".format(Record.objects.first().id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_photo_resize(self):
        file = SimpleUploadedFile("test.jpg", open(os.path.join(STATIC_ROOT, "images/test.jpg"), "rb").read(), "image/jpeg")
        payload = {
            "name_of_fish": "MyTuna",
            "weight": "1.5",
            "length": "1.5",
            "species": "Tuna",
            "latitude": "1.5",
            "longitude": "1.5",
            "photo": file
        }

        record = Record.objects.create(**payload)

        self.assertGreater(record.photo.width, 140)
        self.assertGreater(record.photo.height, 140)

        compress(record.id)

        record.refresh_from_db()

        self.assertEqual(record.photo.width, 140)
        self.assertEqual(record.photo.height, 140)

    def test_get_photo(self):
        # The images are served from the STATIC_ROOT by nginx
        url = "http://nginx" + Record.objects.first().photo.url
        response = request.urlopen(url)

        self.assertEqual(response.status, 200)

