from django.db import models


class Shops(models.Model):
    shop_name = models.CharField(max_length=50, null=False, blank=False)
    shop_location = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return "{0}".format(self.pk)


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False, blank=False)
    parent_cat = models.CharField(max_length=50, null=False, blank=False)
    shop_id = models.ForeignKey(Shops, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return "{0}".format(self.pk)


class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return "{0}".format(self.pk)


class Media(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='children')
    product_image = models.ImageField()

    def __str__(self):
        return "{0}".format(self.pk)
