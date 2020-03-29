from rest_framework import serializers

from products.models import Product


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('seller', 'name', 'price')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('seller', 'name', 'price')
