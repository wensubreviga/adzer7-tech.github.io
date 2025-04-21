from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def hobbies(request):
    return render(request, 'hobbies.html')

def contact(request):
    return render(request, 'contact.html')