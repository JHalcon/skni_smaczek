from django.db import models


# Create your models here.


class ProductType(models.Model):
    product_type = models.CharField(unique=True, max_length=25)

    def __str__(self):
        return '{}'.format(self.product_type)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_type = models.ForeignKey(ProductType, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.product_name, self.product_type)
