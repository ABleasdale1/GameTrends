from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'userApp/home.html')

def profile(request):
    return render(request, 'userApp/profile.html')

def friends(request):
    return render(request, 'userApp/friends.html')

def store(request):
    return render(request, 'userApp/store.html')