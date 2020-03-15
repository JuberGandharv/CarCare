from django.db import models

# Create your models here.
class Picupload(models.Model):
    image_file = models.ImageField(upload_to ='pic_upload',blank = True)
