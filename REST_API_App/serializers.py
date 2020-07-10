from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class ShopsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shops
        fields = ['shop_name', 'shop_location']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'parent_cat', 'shop_id']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'category_id']


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = ['product_id', 'product_image']
