from django.contrib.auth.mixins import PermissionRequiredMixin


class IsAdminPermission(PermissionRequiredMixin):
    """Verify that the user is an admin and is authenticated."""
    def has_permission(self) -> bool:
        return self.request.user.is_authenticated and self.request.user.is_superuser