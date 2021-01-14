from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import RetrieveModelMixin

from tiki.models import Category, Seller, Product, Sell, Image
from tiki.serializers import CategorySerializer, SellerSerializer, ProductSerializer, SellSerializer

class ListAllProductView(ListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class ListCreateProductView(RetrieveModelMixin, ListCreateAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Product successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Product unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteProductView(RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer

    def put(self, request, *args, **kwargs):
        product = get_object_or_404(Product, shop_id=kwargs.get('pk'))
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Product successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Product unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        product = get_object_or_404(Product, shop_id=kwargs.get('pk'))
        product.delete()

        return JsonResponse({
            'message': 'Delete Product successful!'
        }, status=status.HTTP_200_OK)
