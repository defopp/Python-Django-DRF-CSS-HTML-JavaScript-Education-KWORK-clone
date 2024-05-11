from rest_framework.views import APIView   
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


from .models import User
from .serializers import UserSerializer


# TEST API

# class TestUserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserApiView(APIView):    
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
        

