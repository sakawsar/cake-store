from django.db import models

# Create your models here.
class Menu( models.Model ):
    menu_text = models.TextField()
    menu_slug = models.TextField()
    def __str__(self):
        return self.menu_text
class Product( models.Model ):
    # product_id = models.AutoField()
    title = models.TextField()
    product_slug = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # product_image = models.FieldFile()
    # product_image_path = models.FilePathField()
    def __str__(self):
        return self.title