from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductMixinsApiView.as_view()),
    path('<int:pk>/', views.ProductMixinsApiView.as_view()),
    path('<int:pk>/put/', views.ProductMixinsApiView.as_view()),
    path('<int:pk>/destroy/', views.ProductMixinsApiView.as_view()),
]