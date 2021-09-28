from django.urls import path
from .views import AdminDashboard, MemberDashboard

urlpatterns = [
    path('admin/', AdminDashboard.as_view(), name="admin_dashboard"),
    path('member/', MemberDashboard.as_view(), name="member_dashboard")
]
