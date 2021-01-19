from abc import ABC

from rest_framework import serializers
from django.contrib.auth.models import User


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password',)
        write_only_fields = ('username',)

    def validate(self, data):
        # Making sure the username always matches the email
        email = data.get('email', None)
        if email:
            data['username'] = email
        return data


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='Confirm Password', write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')
        try:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            return e

    def validate(self, data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data
