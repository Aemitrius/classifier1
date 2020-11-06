from django.db import models
from check.models import ItemObject
from PIL import pillow

class FruitDatabase(models.Model):
    fruit_id = models.AutoField()
    fruit_name = models.CharField(max_length=50)
    fruit_family = models.CharField(max_length=50)
    fruit_type = models.CharField(max_length=50, null=True, blank=True)
    scientific_name = models.CharField(max_length=100)
    main_vital = models.TextField(max_length=200, blank=True, null=True)
    vital_info = models.TextField(max_length=1000)
    history = models.TextField(max_length=1000, blank=True, null=True)
    tree_info = models.TextField(max_length=1000)
    propagation_details = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

