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
class ListCreateUserView(RetrieveModelMixin, ListCreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new User successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        user = get_object_or_404(User, idUser=kwargs.get('pk'))
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update User successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, idUser=kwargs.get('pk'))
        user.delete()

        return JsonResponse({
            'message': 'Delete User successful!'
        }, status=status.HTTP_200_OK)
