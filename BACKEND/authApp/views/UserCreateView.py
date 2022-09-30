from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializers.serializerUser import SerializadorUser
from authApp.serializers.serializerRol import SerializadorRol

class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = SerializadorUser(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
                "password": request.data["password"]}

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)