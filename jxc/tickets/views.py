from django.views import View
from django.http.response import JsonResponse


class GetTickets(View):
    def get(self, request):
        return JsonResponse({})
