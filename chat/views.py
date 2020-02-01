from django.shortcuts import render, HttpResponse
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

# def test(request):
#     print(request.__dict__)
#     return obtain_jwt_token

