from rest_framework import viewsets

from .models import User
from .serializers import UserCreateSerializer
from .tasks import send_otp_email

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration(request):
    serializer = UserCreateSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        send_otp_email.delay(request.data['email'])
        return Response(UserCreateSerializer(user).data,
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
