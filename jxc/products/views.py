from django.views import View
from utils import model_util
from products.models import ProductInfo
from django.http.response import JsonResponse
from django.forms import model_to_dict


class ProductAction(View):
    def post(self, request):
        obj = ProductInfo()
        model_util.set_dict_to_model(request.data, obj)
        obj.save()
        return JsonResponse({})

    def put(self, request):
        obj = ProductInfo.objects.get(request.data.get('id'))
        model_util.set_dict_to_model(request.data, obj)
        obj.save()
        return JsonResponse({})


class ProductAll(View):
    def get(self, request):
        return JsonResponse([model_to_dict(item) for item in ProductInfo.objects.all()], safe=False)


class ProductSearch(View):
    def get(self, request):
        key = request.data.get('key')
        return JsonResponse([model_to_dict(item) for item in ProductInfo.objects.filter(name__icontains=key)], safe=False)
