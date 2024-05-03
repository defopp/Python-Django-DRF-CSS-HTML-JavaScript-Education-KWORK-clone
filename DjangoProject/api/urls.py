from rest_framework.routers import DefaultRouter

# from messageApp.views import MessageViewSet

router = DefaultRouter()
# router.register('message', MessageViewSet)

urlpatterns = [
    
]

urlpatterns.extend(router.urls)