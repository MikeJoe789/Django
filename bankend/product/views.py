from rest_framework import generics, mixins

from api.mixin import StaffEditerPermissionMix
from .models import Products
from .serializers import ProductsSerializers
# from ..api.permissions import IsStaffEditorPermission
  

class ProductMixinsApiView(
    generics.GenericAPIView, 
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    StaffEditerPermissionMix
    ):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers 
    lookup_field = 'pk'
    # permission_classes = [IsStaffEditorPermission]
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication
    #     ]

    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers 

class ProductListApiView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers  

class ProductCreateApiView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers 

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers   

class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers   