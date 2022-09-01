from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.forms.models import model_to_dict
from product.models import Products
from product.serializers import ProductsSerializers
# Create your views here.

# @api_view(['GET'])
def api_home(request, *args, **kwargs):
    return HttpResponse("request")
    # post_serializer = ProductsSerializers(data=request.data)
    # if post_serializer.is_valid(raise_exception=True):
    #     return Response(post_serializer.data)
