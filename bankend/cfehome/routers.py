from rest_framework.routers import DefaultRouter


from product import viewset

router = DefaultRouter()
router.register('product-v2', viewset.ProductsViewSets, basename='p')
urlpatterns = router.urls
