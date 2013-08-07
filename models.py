from django.db import models

# Create your models here.

class MetaModel(models.Model):
    name = models.CharField(max_length=200)

class Field(models.Model):
    meta_model = models.ForeignKey(MetaModel)
    name = models.CharField(max_length=200)
