from django import forms
from .models import Documents, ELibrary, Module


class ELibraryForm(forms.ModelForm):

    class Meta:
        model=ELibrary
        fields=['title', 'file', 'description']


class DocumentForm(forms.ModelForm):

    class Meta:
        model=Documents
        fields=['title', 'file', 'description']
        

class ModuleForm(forms.ModelForm):

    class Meta:
        model=Module
        fields=['title', 'file', 'description']
