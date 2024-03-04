from django.urls import path

from productsApp.views import MainCategoryView

urlpatterns = [
#     path('signup/', signupView.as_view(), name='signup'),
#     path('login/', loginView.as_view(), name='login'),
#     path('logout/', logoutView.as_view(), name='logout'),
#     path('<int:pk>', profileView.as_view(), name='profile'),

    # path('', catalog.as_view(), name='catalog')
    path('<str:urlname>', MainCategoryView.as_view(), name='catalog')

]
