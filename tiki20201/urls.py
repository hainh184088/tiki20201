"""tiki20201 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tiki import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('tikiapi.urls')),
    # path('category/',views.ListAllCategoryView.as_view()),
    # path('category/<str:pk>', views.ListCreateCategoryView.as_view()),
    # path('category/get/<str:pk>', views.UpdateDeleteCategoryView.as_view()),
    path('seller/',views.ListAllSellerView.as_view()),
    path('seller/<str:pk>', views.ListCreateSellerView.as_view()),
    path('seller/get/<str:pk>', views.UpdateDeleteSellerView.as_view()),
    path('homepage/',views.ListAllCategoryView.as_view()),
    path('product/<str:pk>',views.ListCreateProductView.as_view()),
    path('product/get/<str:pk>',views.UpdateDeleteProductView.as_view()),
]
