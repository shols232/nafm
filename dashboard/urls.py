from django.urls import path
from .views import AdminDashboard

urlpatterns = [
    path('admin/', AdminDashboard.as_view(), name="admin_dashboard"),
]
