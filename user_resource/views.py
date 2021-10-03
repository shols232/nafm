from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .resource_utils import validate_resource_form

from .constants import SAVE_RESOURCE_FAILED_MESSAGE, SAVE_RESOURCE_SUCCESS_MESSAGE

from .forms import DocumentForm, ELibraryForm, ModuleForm
from .permissions import IsAdminPermission
from django.views import View
from django.contrib import messages

from .models import ELibrary, Documents, Module

class ELibraryView(LoginRequiredMixin, View):
    """View for displaying E-libraries for all users."""

    def get(self, request, *args, **kwargs):
        
        return render(request, 'e-library/e-library.html', {'resources': ELibrary.objects.all()})

    def post(self, request, *args, **kwargs):
        return render(request, 'e-library/add-e-library.html', {})


class AddELibraryView(IsAdminPermission, View):
    """View for displaying E-libraries for all users."""
    form = ELibraryForm
    form_initial_values = {'title':''}

    def get(self, request, *args, **kwargs):
        return render(request, 'e-library/add-e-library.html', {'form': self.form(initial=self.form_initial_values)})

    def post(self, request, *args, **kwargs):
        # Check if the form is valid:
        success = validate_resource_form(self.form(request.POST, request.FILES), request, self.form_initial_values)
        if success:
            form = self.form(initial=self.form_initial_values)

        return render(request, 'e-library/add-e-library.html', {'form': form})


class DocumentsView(LoginRequiredMixin, View):
    """View for displaying Documents for all users."""

    def get(self, request, *args, **kwargs):
        return render(request, 'documents/documents.html', {'resources': Documents.objects.all()})


class AddDocumentView(IsAdminPermission, View):
    """View for adding a document as an admin."""
    form = DocumentForm
    form_initial_values = {'title':''}

    def get(self, request, *args, **kwargs):
        return render(request, 'documents/add-document.html', {'form': self.form(initial=self.form_initial_values)})

    def post(self, request, *args, **kwargs):
        # Check if the form is valid:
        success = validate_resource_form(self.form(request.POST, request.FILES), request, self.form_initial_values)
        if success:
            form = self.form(initial=self.form_initial_values)

        return render(request, 'documents/add-document.html', {'form': form})


class ModuleView(LoginRequiredMixin, View):
    """View for displaying Modules for all users."""

    def get(self, request, *args, **kwargs):
        return render(request, 'e-library/e-library.html', {'resources': Module.objects.all()})


class AddModuleView(IsAdminPermission, View):
    """View for adding a module as an admin."""
    form = ModuleForm
    form_initial_values = {'title':''}

    def get(self, request, *args, **kwargs):
        return render(request, 'modules/add-modules.html', {'form': self.form(initial=self.form_initial_values)})

    def post(self, request, *args, **kwargs):
        # Check if the form is valid:
        success = validate_resource_form(self.form(request.POST, request.FILES), request, self.form_initial_values)
        if success:
            form = self.form(initial=self.form_initial_values)

        return render(request, 'modules/add-modules.html', {'form': form})

