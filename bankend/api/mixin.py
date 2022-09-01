from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditerPermissionMix():
    permission_class = [
        permissions.IsAdminUser,
        IsStaffEditorPermission
    ]