from django.urls import path
from .views import (
    AddELibraryView,
    AddModuleView,
    DocumentsView,
    ELibraryView,
    ModuleView,
    AddDocumentView,
)

urlpatterns = [
    path("e-library/", ELibraryView.as_view(), name="e-library"),
    path("e-library/create/", AddELibraryView.as_view(), name="e-library-add"),
    path("modules/", ModuleView.as_view(), name="modules"),
    path("module/create/", AddModuleView.as_view(), name="module-add"),
    path("documents/", DocumentsView.as_view(), name="documents"),
    path("documents/create/", AddDocumentView.as_view(), name="document-add"),
]
