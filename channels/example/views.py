from django.shortcuts import render

# Create your views here.

def user_list(request):
    return render(request, 'example/user_list.html')