from django.template.loader import render_to_string
from django.contrib import messages


def izitoast(request, model, message):
    template = None
    if model == "success":
        template = 'custom_response/mul-success-response.txt'
    elif model == "info":
        template = 'custom_response/mul-info-response.txt'
    elif model == "warning":
        template = 'custom_response/mul-warning-response.txt'
    elif model == "danger":
        template = 'custom_response/mul-error-response.txt'

    create_content = render_to_string(template_name=template, context=message)

    if model == "success":
        return messages.success(request=request, message=create_content)
    elif model == "info":
        return messages.info(request=request, message=create_content)
    elif model == "warning":
        return messages.warning(request=request, message=create_content)
    elif model == "danger":
        return messages.error(request=request, message=create_content)
