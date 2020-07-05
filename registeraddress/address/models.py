from django.db import models

# Create your models here.


class Address(models.Model):
    cep = models.CharField(max_length=8)
    address = models.CharField(max_length=80)
    number = models.CharField(max_length=50)
    complement = models.CharField(max_length=1000, blank=True, null=True)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cep