from django.shortcuts import render

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
    return render(request, 'mainApp\\user_profile.html')

def MessengerPage(request):
    return render(request, 'mainApp\\messenger.html')
