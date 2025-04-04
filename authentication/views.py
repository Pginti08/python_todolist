from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import SignupSerializer, LoginSerializer


CustomUser = get_user_model()

@api_view(['POST'])
def signup_view(request):
    """User signup view with validation."""
    serializer = SignupSerializer(data=request.data)  #
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    """User login view that returns JWT tokens."""
    serializer = LoginSerializer(data=request.data)  # ✅ Use request.data
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        return Response({
            'data': {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'id': user.id,
                'email': user.email,
                'username': user.username,
            }
        })
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
