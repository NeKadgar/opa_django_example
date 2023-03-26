import requests
from django.http import HttpResponseForbidden

def opa_authorization(policy: str):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            print(request, policy)

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
