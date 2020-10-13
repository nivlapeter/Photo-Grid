from django.test import TestCase
from .models import Uploader,Image,Location
import datetime as dt

# Create your tests here.
class UploaderTestCase(TestCase):
    #setUp method
    def setUp(self):
        self.uploader=Uploader(1,'John','Doe','examle@gmail.com', 1234567890)

    def test_save_uploader(self):
        self.uploader.save_uploader()
        q_object=Uploader.objects.get(firtst_name='John')
        self.assertEqual(q_object.first_name,'John')
