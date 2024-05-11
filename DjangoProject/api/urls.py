from rest_framework.routers import DefaultRouter
from django.urls import path

# from messageApp.views import 
# from usersApp.api import UserApiView
from messageApp.api import ChatRoomAPI



router = DefaultRouter()
# router.register('message', TestViewSet, basename='TestSet')
# router.register('user', UserApiView.as_view(), basename='TestUserSet')

urlpatterns = [
    # path('users/', UserApiView.as_view(), name='usersAPI')
    path('chatroom/', ChatRoomAPI.as_view(), name='chatroomAPI')
]

urlpatterns.extend(router.urls)