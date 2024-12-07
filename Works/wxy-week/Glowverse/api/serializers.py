from rest_framework import serializers
# from relationship_app.models import User --wrong approach
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
