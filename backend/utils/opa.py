import requests
from rest_framework import status
from django.http import HttpResponseForbidden, HttpRequest, HttpResponseServerError

from apps.users.models import User


class ErrorOpaUpdate(Exception):
    ...


def set_opa_data(path: str, instance_data):
    response = requests.put(f"http://localhost:8181/v1/data/{path}", json=instance_data)
    if response.status_code != status.HTTP_204_NO_CONTENT:
        raise ErrorOpaUpdate


def opa_authorization(instance_name: str):
    def decorator(view_func):
        def wrapper(request: HttpRequest, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden()

            user: User = request.user
            data = {
                "input": {
                    "method": request.method,
                    "user": {
                        "role": user.role,
                        "company_id": user.company.pk if user.company is not None else None,
                        "team_id": user.team.pk if user.team is not None else None
                    },
                    "data": request.data,
                    "instance_name": instance_name
                }
            }
            try:
                response = requests.post("http://localhost:8181/v1/data/rbac/allow", json=data)
                if response.json().get("result", False):
                    return view_func(request, *args, **kwargs)
            except requests.exceptions.RequestException as e:
                return HttpResponseServerError(str(e))

            return HttpResponseForbidden()
        return wrapper
    return decorator
