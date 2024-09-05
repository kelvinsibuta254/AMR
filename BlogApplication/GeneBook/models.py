from django.db import models

# Create your models here.
class GeneBank(models.Model):
    sample_id = models.CharField(max_length=10)
    barcode_sequence = models.CharField(max_length=100)
    primer_sequence = models.CharField(max_length=50)
    gene = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    description = models.TextField(max_length=100)