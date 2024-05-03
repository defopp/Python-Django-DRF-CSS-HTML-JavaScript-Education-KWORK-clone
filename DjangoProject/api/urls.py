from rest_framework.routers import DefaultRouter

# from messageApp.views import 
from usersApp.views import TestUserViewSet

router = DefaultRouter()
# router.register('message', TestViewSet, basename='TestSet')
router.register('user', TestUserViewSet, basename='TestUserSet')

urlpatterns = [
    
]

urlpatterns.extend(router.urls)