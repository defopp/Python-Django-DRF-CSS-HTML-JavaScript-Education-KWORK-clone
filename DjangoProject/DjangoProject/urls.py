"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from mainApp.views import MainPage, ToFreelancerPage, CategoryPage, CategoryCatalogPage, ProjectPage, ProjectCreatePage, UserProfilePage, MessengerPage
# from usersApp.views import ApiSignUp, ApiSignIn



urlpatterns = [
    # main pages
    path('admin/', admin.site.urls),
    path('', MainPage, name='main'),
    path('to_freelancer/', ToFreelancerPage, name='freelancer'),
    path('create_project/', ProjectCreatePage),
    
    
    # pages moded with api
    path('category/', CategoryPage),
    path('category/catalog/', CategoryCatalogPage),
    path('project/', ProjectPage),
    path('user_profile/', UserProfilePage),
    path('messenger/', MessengerPage),
    
    
    
    path('users/', include('usersApp.urls'))
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
