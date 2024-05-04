from rest_framework.routers import DefaultRouter
from django.urls import path

# from messageApp.views import 
# from usersApp.views import UserApiView

router = DefaultRouter()
# router.register('message', TestViewSet, basename='TestSet')
# router.register('user', UserApiView.as_view(), basename='TestUserSet')

urlpatterns = [
    # path('users/', UserApiView.as_view(), name='usersAPI')
]

urlpatterns.extend(router.urls)