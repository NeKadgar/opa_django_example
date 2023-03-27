import requests
from django.http import HttpResponseForbidden, HttpRequest, HttpResponseServerError

from apps.users.models import MyUser


def opa_authorization(policy: str):
    def decorator(view_func):
        def wrapper(request: HttpRequest, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden()

            user: MyUser = request.user
            data = {
                "input": {
                    "method": request.method,
                    "user": {
                        "is_superuser": user.is_superuser,
                        "role": user.role,
                        "companies_owned": [company.name for company in user.companies.all()]
                    },
                    "data": request.data
                }
            }
            try:
                policy_path = '/'.join(policy.split('.'))
                response = requests.post(f"http://localhost:8181/v1/data/{policy_path}", json=data)
                if response.json().get("result", False):
                    return view_func(request, *args, **kwargs)
            except requests.exceptions.RequestException as e:
                return HttpResponseServerError(str(e))

            return HttpResponseForbidden()
        return wrapper
    return decorator
