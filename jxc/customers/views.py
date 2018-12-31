from django.http.response import JsonResponse
from django.views import View
from django.forms.models import model_to_dict
from customers.models import Customer
from utils import model_util

"""
need custom info 


"""


class CustomerAction(View):
    def post(self, request):
        data = request.data
        cus = Customer()
        cus.active = True
        model_util.set_dict_to_model(data, cus)
        cus.save()
        return JsonResponse({})

    def put(self, request):
        custom_id = request.data.get("id")
        cus = Customer.objects.get(custom_id)
        model_util.set_dict_to_model(request.data, cus)
        cus.save()
        return JsonResponse({})


class Customers(View):
    def post(self, request):
        return JsonResponse([model_to_dict(item) for item in Customer.objects.all()], safe=False)


class CustomerSearch(View):
    def post(self, request):
        key = request.data.get('key')
        return JsonResponse([model_to_dict(item) for item in Customer.objects.filter(name__icontains=key)], safe=False)
