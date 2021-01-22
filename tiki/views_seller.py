from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import RetrieveModelMixin
from django.db import connection
from tiki.models import Category, Seller, Product, Sell, Image, User
from tiki.serializers import CategorySerializer, SellerSerializer, ProductSerializer, SellSerializer, CategoryProductSerializer, UserSerializer

class ListAllSellerView(ListCreateAPIView):
    model = Seller
    serializer_class = SellerSerializer
    # def get(self, request, *args, **kwargs):
    #     with connection.cursor() as cursor:
    #         cursor = connection.cursor()
    #         cursor.execute('''SELECT * FROM end_term.seller, end_term.sell, end_term.product where end_term.seller.shop_id = end_term.sell.seller_id and end_term.sell.p_id = end_term.product.id''')
    #         row = cursor.fetchall()
    #         return JsonResponse(row, safe = False)
    def get_queryset(self):
        return Seller.objects.filter()
class ListCreateSellerView(RetrieveModelMixin, ListCreateAPIView):
    model = Seller
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = SellerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Seller successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Seller unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteSellerView(RetrieveUpdateDestroyAPIView):
    model = Seller
    serializer_class = SellerSerializer

    def put(self, request, *args, **kwargs):
        seller = get_object_or_404(Seller, shop_id=kwargs.get('pk'))
        serializer = SellerSerializer(seller, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Seller successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Seller unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        seller = get_object_or_404(Seller, shop_id=kwargs.get('pk'))
        seller.delete()

        return JsonResponse({
            'message': 'Delete Seller successful!'
        }, status=status.HTTP_200_OK)
