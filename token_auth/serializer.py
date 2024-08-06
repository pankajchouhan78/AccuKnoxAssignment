from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from app.models import Person


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("name", "email", "password")

    def create(self, validated_data):
        password = validated_data.get("password", None)
        user = Person.objects.create(**validated_data)
        if password is not None:
            user.password = make_password(password)
            user.save()
        return user


class VarifyUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            person = Person.objects.get(email=data.get('email'))
        except Person.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
        if person.otp != data.get('otp'):
            raise serializers.ValidationError("please Enter valid OTP")

        person.is_varified = True
        person.save()
        return person

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)

    def validate_email(self, email):
        try:
            user = Person.objects.get(email=email)
        except Person.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
        if not user.is_varified:
            raise serializers.ValidationError("User has no permissions to login")
        
        return email


class VarifySerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            person = Person.objects.get(email=data.get('email'))
        except Person.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
        if person.otp != data.get('otp'):
            raise serializers.ValidationError("please Enter valid OTP")

        return person
        
