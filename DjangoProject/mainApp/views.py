from django.shortcuts import render

# Create your views here.
def MainPage(request):
    return render(request, 'mainApp\index.html')
    