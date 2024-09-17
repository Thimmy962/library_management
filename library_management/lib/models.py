from django.db import IntegrityError
from rest_framework import response, status, serializers
from .utils import manageuser

class Members(manageuser.CustomUser):
    def save(self, *args, **kwargs):
        if not self.pk and not self.check_password(self.password):
            self.set_password(self.password)
            self.role = manageuser.CustomUser.Role.MEMBER
        return super().save(*args, **kwargs)
    

class Staffs(manageuser.CustomUser):
    def save(self, *args, **kwargs):
        if not self.pk and not self.check_password(self.password):
            self.set_password(self.password)
            self.role = manageuser.CustomUser.Role.STAFF
        return super().save(*args, **kwargs)

  
class Librarian(manageuser.CustomUser):
    def save(self, *args, **kwargs):
        if not self.pk and not self.check_password(self.password):
            self.set_password(self.password)
            self.role = manageuser.CustomUser.Role.LIBRARIAN
        return super().save(*args, **kwargs)