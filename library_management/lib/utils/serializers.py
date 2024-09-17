# serializers.py
from rest_framework import serializers
from ..models import Members, Staffs
from django.db import IntegrityError


class GetMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ["email", "first_name", "last_name"]

class PostMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"
    

class PostStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = "__all__"

class GetStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = ["email", "first_name", "last_name"]