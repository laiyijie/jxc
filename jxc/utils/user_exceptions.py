from django.http import JsonResponse


class UserErrorException(Exception):
    def __init__(self, status_code=0, error_msg=""):
        self.status_code = status_code
        self.error_msg = error_msg
        self.response = JsonResponse({"code": status_code, "msg": error_msg}, status=417)


class UserWarningException(Exception):
    def __init__(self, status_code=0, error_msg=""):
        self.status_code = status_code
        self.error_msg = error_msg
        self.response = JsonResponse({"msg": error_msg}, status=417)
