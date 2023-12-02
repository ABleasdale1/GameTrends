from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'userApp/home.html')

def profile(request):
    userDetails = {
        'username' : 'sysAdmin',
        'email' : 'admin@gametrends.com',
        'fName' : 'System',
        'lName' : 'Admin',
        'country' : 'United Kingdom',
        'city' : 'London',
        'address' : '123 Fake Street',
        'postcode' : 'AB1 2CD',
    }
    return render(request, 'userApp/profile.html', context=userDetails)

def friends(request):
    return render(request, 'userApp/friends.html')

def store(request):
    return render(request, 'userApp/store.html')