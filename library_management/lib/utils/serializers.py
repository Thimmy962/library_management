# serializers.py
from ..utils import manageuser
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers, status
from .. import models



class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = "__all__"

    def get_permissions(self, obj):
        return [permission.name for permission in obj.permissions.all()]

    def validate_name(self, value):
        # Clean the name field
        cleaned_value = value.strip().title()
        if models.Group.objects.filter(name=cleaned_value).exists():
            raise serializers.ValidationError("A group with this name already exists.")
        return cleaned_value

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
"""
    The below has to do with Non human entities
"""


class GetMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Members
        fields = ["id", "email", "first_name", "last_name"]


class PostMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Members
        fields = "__all__"

    def validate_email(self, value):
        if manageuser.CustomUser.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError({"message": "A user with this email already exists."})
        return value


class PostStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staffs
        fields = "__all__"

    def validate_email(self, value):
        if manageuser.CustomUser.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError({"message": "A user with this email already exists."})
        return value


class GetStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staffs
        fields = ["id", "email", "first_name", "last_name"]



class PostLibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Librarian
        fields = "__all__"   

    def validate_email(self, value):
        if manageuser.CustomUser.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError({"message": "A user with this email already exists."})
        return value


class GetLibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Librarian
        fields = ["email", "first_name", "last_name"]
    

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genres
        fields = "__all__"


    def validate_name(self, value):
        # Clean the name field
        cleaned_value = value.strip().title()

        # Check if the cleaned name already exists in the database
        if models.Genres.objects.filter(name=cleaned_value).exists():
            raise serializers.ValidationError("A genre with this name already exists.")

        return cleaned_value



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Authors
        fields = "__all__"

    def validate(self, data):
        if "first_name" in data:
            data["first_name"] = data["first_name"].strip().title()
        if "last_name" in data:
            data["last_name"] = data["last_name"].strip().title()
        if models.Authors.objects.filter(
            first_name=data["first_name"], 
            last_name=data["last_name"]
        ).exists():
            raise serializers.ValidationError(
                "Author with this name already exists"
            )
        return data


"""
    The below has to do with Non human entities
"""

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    class Meta:
        model = models.Books  # Ensure you're using the correct model
        fields = "__all__"  # Initially, we define that we'll use all fields

    
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')

        if request and request.method != 'GET':
            # Retain only specific fields for non-POST requests
            fields = {
                    'id': fields['id'],
                    'book_name': fields['book_name'],
                    'authors': fields['authors'],
                    'genres': fields['genres'],
                }
        return fields
    
    def get_authors(self, obj):
        # This method will be called to get the serialized authors data
        return [f"{author.first_name} {author.last_name}" for author in obj.authors.all()]
    
    def get_genres(self, obj):
        return [f"{genre.name}" for genre in obj.genres.all()]

    def validate_book_name(self, value):
        # Clean and validate the book name
        return value.strip().title()
