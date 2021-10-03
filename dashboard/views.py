from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from user_resource.permissions import IsAdminPermission


class AdminDashboard(IsAdminPermission, View):
    """Dashboard view for admin user."""

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'dashboard/admin_dashboard.html', context)

class MemberDashboard(LoginRequiredMixin, View):
    """Dashboard view for users."""

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'dashboard/member_dashboard.html', context)