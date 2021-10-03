from django.urls import path
from .views import DocumentsView, ELibraryView, ModuleView

urlpatterns = [
    path('e-library/', ELibraryView.as_view(), name="e-library"),
    path('modules/', ModuleView.as_view(), name="modules"),
    path('documents/', DocumentsView.as_view(), name="documents"),
]
