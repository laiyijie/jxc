from repos.models import Repo
from django.views import View
from django.http.response import JsonResponse
from utils import model_util
from django.forms import model_to_dict


class RepoAction(View):
    def post(self, request):
        obj = Repo()
        model_util.set_dict_to_model(request.data, obj)
        obj.save()
        return JsonResponse(model_to_dict(obj))

    def put(self, request):
        obj = Repo.objects.get(request.data.get("id"))
        model_util.set_dict_to_model(request.data, obj)
        obj.save()
        return JsonResponse(model_to_dict(obj))


class Repos(View):
    def get(self, request):
        return JsonResponse([model_to_dict(item) for item in Repo.objects.all()], safe=True)


class RepoSearch(View):
    def get(self, request):
        key = request.data.get("key")
        return JsonResponse([model_to_dict(item) for item in Repo.objects.filter(name__icontains=key)], safe=False)
