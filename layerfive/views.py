from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserDescription
from .serializers import UserDescriptionSerializer


class CreateUserDescription(APIView):

    def get(self, request, format=None):
        users = UserDescription.objects.all()
        serializer = UserDescriptionSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print(request.data)
        serializer = UserDescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
