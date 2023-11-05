from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from django.shortcuts import get_object_or_404
from . models import CustomUser
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from django.http import JsonResponse
from rest_framework.views import APIView
from oauth2_provider.decorators import protected_resource
 
class UserListView(APIView):
 permission_classes = [IsAuthenticated]
 
 def get(self, request):
         print(request.user)
         queryset = CustomUser.objects.all()
         serializer = UserRegistrationSerializer(queryset, many=True)
         return Response(serializer.data)
 
class UserRegisterView(APIView): 
 permission_classes = [AllowAny] 
 def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class UserViewDetails(APIView):
  def get(self, request,id):
    user = get_object_or_404(CustomUser,pk=id)
    serializer = UserRegistrationSerializer(user)
    return Response(serializer.data)
  def put(self,request,id):
      user = get_object_or_404(CustomUser,pk=id)
      serializer = UserRegistrationSerializer(user, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
  def delete(self,request,id):
    pass
