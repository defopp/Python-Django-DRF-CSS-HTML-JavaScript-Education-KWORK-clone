from django.shortcuts import render

# Create your views here.
def MainPage(request):
    return render(request, 'mainApp\\main.html')

def ToFreelancerPage(request):
    return render(request, 'mainApp\\to_freelancer.html')

def CategoryPage(request):
    return render(request, 'mainApp\\category.html')

def CategoryCatalogPage(request):
    return render(request, 'mainApp\\category_catalog.html')

def ProjectPage(request):
    return render(request, 'mainApp\\project.html')
