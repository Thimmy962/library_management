from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Staffs)
admin.site.register(models.Members)
admin.site.register(models.Librarian)