from django.shortcuts import render

from utils.user_exceptions import *
from users.models import *
from django.views import View


def login_session_save(session, user):
    session["userid"] = user.id
    session.save()


class UserLogin(View):
    def post(self, request):
        session = request.session
        username = request.data.get('username')
        password = request.data.get('password')

        user_id = User.objects.auth(username, password)
        if user_id is None:
            raise UserWarningException(1003, "用户名或密码错误")
        user = User.objects.get(id=user_id)

        login_session_save(session, user)
        return JsonResponse({
            "userid": user_id,
        })


class UserLogout(View):
    def post(self, request):
        request.session.clear()
        return JsonResponse({})
