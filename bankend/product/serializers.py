from rest_framework import serializers
from .models import Products


class ProductsSerializers(serializers.ModelSerializer):

    myUrl = serializers.SerializerMethodField(read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Products
        fields = [
            'pk',
            'title',
            'email',
            'content',
            'price',
            'discount',
            'myUrl'
        ]

    def create(self, validated_data):
        email = validated_data.pop('email')
        obj= super().create(validated_data)
        print(email)
        return obj

    def get_myUrl(self, obj):
        return f'api/product/{obj.pk}'

    def get_discount(self, obj):
        discount = float(obj.price) * 0.8
        return '%.2f' % discount