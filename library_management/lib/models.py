from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from .utils import manageuser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType



class Members(manageuser.CustomUser):
    def save(self, *args, **kwargs):
        if not self.pk and not self.check_password(self.password):
            self.set_password(self.password)
            self.role = manageuser.CustomUser.Role.MEMBER
        return super().save(*args, **kwargs)
    

class Staffs(manageuser.CustomUser):
    def save(self, *args, **kwargs):
        # First-time save: setting is_staff, password, and role
        if not self.pk and not self.check_password(self.password):
            self.email = self.email.lower()
            self.set_password(self.password)
            self.role = manageuser.CustomUser.Role.STAFF
            self.is_staff = True
        return super().save(*args, **kwargs)



class Librarian(manageuser.CustomUser):
    def save(self, *args, **kwargs):
        # First-time save: setting is_staff, is_superuser, password, and role
        if not self.pk and not self.check_password(self.password):
            self.is_superuser = True
            self.is_staff = True
            self.set_password(self.password)
            self.role = manageuser.CustomUser.Role.LIBRARIAN
        
        # Save the Librarian instance
        super().save(*args, **kwargs)
        
        staff_manager, created = Group.objects.get_or_create(name = "StaffManager")
        staff_content_type = ContentType.objects.get_for_model(Staffs)
        staff_permissions = Permission.objects.filter(content_type = staff_content_type)
        # add all the permissions in the staff_permission to the staff manager grp
        staff_manager.permissions.add(*staff_permissions)
        # add the created librarian instance to the stafff_manager grp
        self.groups.add(staff_manager)


class Authors(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=32, null=False, blank=False)


class Genres(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)


class Books(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    author = models.ManyToManyField(Authors, related_name="this_authors_books")
    genres = models.ManyToManyField(Genres, related_name="this_genres_books")
    synopsis = models.TextField(max_length=2048)



class Review(models.Model):
    class StarRating(models.IntegerChoices):
        FIVE_STARS = 5, "5"
        FOUR_STARS = 4, "4"
        THREE_STARS = 3, "3"
        TWO_STARS = 2, "2"
        ONE_STAR = 1, "1"

    # Reviewer relationship
    reviewer = models.ForeignKey('Members', on_delete=models.DO_NOTHING, related_name="reviews")
    # Generic foreign key fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # Rating and comment
    rating = models.IntegerField(choices=StarRating.choices, null=True)
    comment = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)