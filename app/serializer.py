from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Person


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


# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=50)
#     password = serializers.CharField(max_length=100)

#     def validate(self, data):
#         email = data.get('email')
#         if Person.objects.filter(email=email).exists():
#             password = data.get('password')
#             user = authenticate(email=email, password=password)
#             if user is None:
#                 return serializers.ValidationError("Invalid password")
#             return user
#         else:
#             return  serializers.ValidationError("Invalid Username")


class PersonSerializer(serializers.ModelSerializer):
    # friends = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='friends-detail')
    friends = serializers.StringRelatedField(many=True, read_only=True)
    sent_requests = serializers.StringRelatedField(many=True, read_only=True)
    received_requests = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="email"
    )

    """
    StringRelatedField main default me name ko return kiya jata hai.
    SlugRelatedField me email show hoga slug_field se

    """

    class Meta:
        model = Person
        fields = (
            "id",
            "name",
            "email",
            "friends",
            "sent_requests",
            "received_requests",
        )

    """
    this method for count the number of friends, count the number of sent requests, and count the number of received requests
    """
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["friends_count"] = instance.friends.count()
        representation["sent_requests_count"] = instance.sent_requests.count()
        representation["received_requests_count"] = instance.received_requests.count()
        return representation


class SentRequestSerializer(serializers.Serializer):
    to_request = serializers.IntegerField()


class AcceptRequestSerializer(serializers.Serializer):
    accept_request = serializers.IntegerField()
