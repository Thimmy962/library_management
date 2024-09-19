# serializers.py
from rest_framework import serializers
from .. import models 
from django.contrib.contenttypes.models import ContentType



class GetMemberSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()
    class Meta:
        model = models.Members
        fields = ["id","email", "first_name", "last_name", "content_type"]

    def get_content_type(self, obj):
        return ContentType.objects.get_for_model(obj).id


class PostMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Members
        fields = "__all__"
    



class PostStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staffs
        fields = "__all__"


class GetStaffSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()
    class Meta:
        model = models.Staffs
        fields = ["email", "first_name", "last_name", "content_type"]

    
    def get_content_type(self, obj):
        return ContentType.objects.get_for_model(models.Staffs).id




class PostLibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Librarian
        fields = "__all__"




class GetLibrarianSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = models.Librarian
        fields = ["email", "first_name", "last_name", "content_type"]

    def get_content_type(self, obj):
        return ContentType.objects.get_for_model(models.Librarian).id
    

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genres
        fields = "__all__"


class AuthorSerializer(serializers.SerializerMethodField):
    class Meta:
        model = models.Authors
        fields = "__all__"