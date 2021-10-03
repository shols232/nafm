from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .models import ELibrary, Documents, Module

class ELibraryView(LoginRequiredMixin, View):
    """View for displaying E-libraries for all users."""

    def get(self, request, *args, **kwargs):
        
        return render(request, 'e-library/e-library.html', {'resources': ELibrary.objects.all()})


class DocumentsView(LoginRequiredMixin, View):
    """View for displaying Documents for all users."""

    def get(self, request, *args, **kwargs):
        
        return render(request, 'e-library/e-library.html', {'resources': Documents.objects.all()})


class ModuleView(LoginRequiredMixin, View):
    """View for displaying Modules for all users."""

    def get(self, request, *args, **kwargs):
        
        return render(request, 'e-library/e-library.html', {'resources': Module.objects.all()})

