from rest_framework import status
from rest_framework.views import APIView
from myapp.models import User,PowerPosition
from .serializers import UserSerializer,PowerPositionSerializer
from rest_framework.response import Response
# Create your views here.


class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        user = request.data
        serializer = UserSerializer(data=user)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            return Response("您输入的数据有错误")
        serializer.save()
        return Response(serializer.validated_data,status=status.HTTP_201_CREATED)


class Test(APIView):
    def get(self, request):
        powers = PowerPosition.objects.filter(parent__isnull=True)
        serializer = PowerPositionSerializer(instance=powers, many=True)
        return Response(serializer.data)
