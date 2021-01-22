from tiki.views_seller import *
from tiki.views_product import *
from django.db import connection, transaction
from django.http import JsonResponse
from django.views.generic import TemplateView 
import json
# def save_data(request):
#       if request.method == 'POST':
#     json_data = json.loads(request.body)
#     try:
#       data = json_data['data']
#     except KeyError:
#       return HttpResponseServerError("Malformed data!")
#     return HttpResponse("Got json data")
class AboutView(TemplateView):
    template_name = "about.html"

class ListAllCategoryProductView(ListCreateAPIView):
    model = Category
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return Category.objects.all()[:5]
 
class ListCreateCategoryProductView(RetrieveModelMixin, ListCreateAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategoryProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = CategoryProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Category successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Category unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class ListAllCategoryView(ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class ListCreateCategoryView(RetrieveModelMixin, ListCreateAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Category successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Category unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteCategoryView(RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer

    def put(self, request, *args, **kwargs):
        category = get_object_or_404(Category, idCategory=kwargs.get('pk'))
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Category successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Category unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        category = get_object_or_404(Category, idCategory=kwargs.get('pk'))
        category.delete()

        return JsonResponse({
            'message': 'Delete Category successful!'
        }, status=status.HTTP_200_OK)
