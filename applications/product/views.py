from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from applications.product.models import Product
from applications.product.serializer import ProductSerializer



class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# class ProductListApiView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductCreateApiView(CreateAPIView):
#     serializer_class = ProductSerializer
#     # permission_classes = [IsAuthenticated]
#     # permission_classes = [IsAdminUser]

# class ProductDetailApiView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
