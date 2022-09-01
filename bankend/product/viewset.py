from rest_framework import viewsets


from .models import Products
from .serializers import ProductsSerializers


class ProductsViewSets(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers 
    lookup_field = 'pk'
