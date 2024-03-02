from django.urls import path

from usersApp.views import loginView, signupView, logoutView, profileView

urlpatterns = [
    path('signup/', signupView.as_view(), name='signup'),
    path('login/', loginView.as_view(), name='login'),
    path('logout/', logoutView.as_view(), name='logout'),
    path('<int:pk>', profileView.as_view(), name='profile'),
]
