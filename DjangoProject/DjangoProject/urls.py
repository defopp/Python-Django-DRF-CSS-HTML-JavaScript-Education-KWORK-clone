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


from mainApp.views import MainPage, ToFreelancerPage
from messageApp.views import ChatView


urlpatterns = [
    # main pages
    path('admin/', admin.site.urls),
    path('', MainPage, name='main'),
    path('to_freelancer/', ToFreelancerPage, name='freelancer'),
    
    # api
    path('api/', include('api.urls')),
    
    # views
    path('users/', include('usersApp.urls')),
    path('projects/', include('productsApp.urls')),
    path('messages', ChatView.as_view(), name="chat")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    