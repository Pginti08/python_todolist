from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
import re
from django.utils.translation import gettext as _


CustomUser = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)  # Validates email format

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']



    def create(self, validated_data):
        """Create and return a new user with encrypted password."""
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=5,
        max_length=10,
        error_messages={
            "blank": "Password cannot be empty.",
            "min_length": "Password too short.",
        },
    )

    def validate(self, data):
        """Authenticate user using email instead of username."""
        email = data.get("email")
        password = data.get("password")

        # if email and password:
        user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

        if not user:
            raise serializers.ValidationError({'error': 'Unable to log in with provided credentials.'})

        data['user'] = user
        return data