from django.contrib import messages
from .constants import SAVE_RESOURCE_FAILED_MESSAGE, SAVE_RESOURCE_SUCCESS_MESSAGE

def validate_resource_form(form, request, initial) -> bool:
    """
    Validate resource form, and add appropriate messages to current request object.
    
    :return bool:
    """
    # Check if the form is valid:
    if form.is_valid():
        resource = form.save(commit=False)
        resource.owner = request.user
        resource.save()
        messages.success(request, SAVE_RESOURCE_SUCCESS_MESSAGE)
        return True
    else:
        messages.error(request, SAVE_RESOURCE_FAILED_MESSAGE)
        return False
