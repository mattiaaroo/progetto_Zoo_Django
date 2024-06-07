from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})

def animal_details(request):
    return render(request, "pages/animal_details.html", {})

def add_animal(request):
    return render(request, "pages/add_animal.html", {})

def rm_animal(request):
    return render(request, "pages/rm_animal.html", {})

def guardians(request):
    return render(request, "pages/guardians.html", {})

def guardian_deatils(request):
    return render(request, "pages/guardian_details.html", {})

def feed_animal(request):
    return render(request, "pages/feed_animal.html", {})

def clear_fence(request):
    return render(request, "pages/clear_fence.html", {})