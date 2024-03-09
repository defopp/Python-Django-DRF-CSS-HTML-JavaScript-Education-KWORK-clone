from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session

from productsApp.models import Product



# Create your views here.
def MainPage(request, context = None):
    return render(request, 'mainApp\\main.html', )

def ToFreelancerPage(request):
    return render(request, 'mainApp\\to_freelancer.html')

def CategoryPage(request):
    return render(request, 'mainApp\\category.html')

def CategoryCatalogPage(request):
    return render(request, 'mainApp\\category_catalog.html')

def ProjectPage(request):
    return render(request, 'mainApp\\project.html')

def ProjectCreatePage(request):
    return render(request, 'mainApp\\project_create.html')

def UserProfilePage(request):
    if request.user.is_authenticated:
        owner_projects = Product.objects.all().filter(owner_id=request.user.id)
        return render(request, 'mainApp\\user_profile.html', {'owner_projects':owner_projects})
    else:
        return redirect('main')

def MessengerPage(request):
    return render(request, 'mainApp\\messenger.html')
