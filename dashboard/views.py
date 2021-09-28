from django.shortcuts import render
from django.views import View

class AdminDashboard(View):
    """Dashboard view for admin user."""

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'dashboard/admin_dashboard.html', context)

class MemberDashboard(View):
    """Dashboard view for users."""

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'dashboard/member_dashboard.html', context)