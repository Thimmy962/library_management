# serializers.py
from ..utils import manageuser
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers, status
from .. import models


def validate_email(value):
        if manageuser.CustomUser.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError({"message": "A user with this email already exists."})
        return


class GroupSerializer(serializers.SerializerMethodField):
    class Meta:
        model = Group
        fields = "__all__"


class PermissionSerializer(serializers.SerializerMethodField):
    class Meta:
        model = Permission
        fields = "__all__"
"""
    The below has to do with Non human entities
"""


class GetMemberSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()
    class Meta:
        model = models.Members
        fields = ["id", "email", "first_name", "last_name", "content_type"]

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
        return ContentType.objects.get_for_model(obj).id


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


    def clean_data(self, data):
        if "name" in data:
            data["name"] = data["name"].strip().title()
        return data



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Authors
        fields = "__all__"

    def clean_data(self, data):
        if "first_name" in data:
            data["first_name"] = data["first_name"].strip().title()
        if "last_name" in data:
            data["last_name"] = data["last_name"].strip().title()
        return data


"""
    The below has to do with Non human entities
"""
class BooKSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = "__all__"


    def clean_data(self, data):
        if "booK_name" in data:
            data["book_name"] = data["book_name"].strip().title()
        return data
    

    def add_genres(self, genre_list):
        for genre in genre_list:
            this_genre = models.Genre.objects.get(pk = int(genre))
            self.genres.add(this_genre)

    
    def add_authors(self, author_list):
        for author in author_list:
            this_genre = models.Genre.objects.get(pk = int(author))
            self.genres.add(this_genre)