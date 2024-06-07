import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token as get_csrf_token

# Create your views here.

def csrf(request):
    return JsonResponse({'csrfToken': get_csrf_token(request)})


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"detail": "Success",
                             "status": 200,
                             'user': f"{user.first_name} {user.last_name}"},
                            status=200)
    return JsonResponse({"detail": "Invalid credentials",
                         "status": 400},
                        status=400)


def logout_view(request):
    logout(request)
    return JsonResponse({"detail": "Success", "status": 200}, status=200)


def is_logged_in(request):
    user = request.user
    first_name = ''
    last_name = ''

    if user.is_authenticated:
        first_name = user.first_name
        last_name = user.last_name

    return JsonResponse({"is_authenticated": user.is_authenticated,
                         "status": 200,
                         'user': f"{first_name} {last_name}"
                         })