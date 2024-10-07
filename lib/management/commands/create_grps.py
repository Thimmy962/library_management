# your_app/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from lib import models

class Command(BaseCommand):
    help = 'Create necessary groups and assign permissions'

    def handle(self, *args, **kwargs):
        # get this group
        staff_group, created = Group.objects.get_or_create(name="StaffManager")
        # get the content type of this model staff
        staff_content_type = ContentType.objects.get_for_model(models.Staffs)
        # get the permissions associated with a staff model(CRUD of stff)
        staff_permissions = Permission.objects.filter(content_type=staff_content_type)
        # add permissions associated with staff to the group created
        staff_group.permissions.add(*staff_permissions)

        self.stdout.write(self.style.SUCCESS(f'New groups created'))
