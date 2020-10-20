from rest_framework import serializers
from django.contrib.auth.models import User
from TripPlannerApp.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            "id",
            "name",
            "budget",
            "no_of_days",
            "created_at",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True}
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password"
        ]

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User(username=self.validated_data['username'],
                    email=self.validated_data['email']
                    )
        password=self.validated_data['password']
        # password_confirm=self.validated_data['password_confirm']

        # if password != password_confirm:
        #     raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()

        return user
