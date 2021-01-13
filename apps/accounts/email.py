from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from .token import account_activation_token


def send_success_activation_email(request, user):
    """ Send a letter of successful account confirmation """

    current_site = get_current_site(request)
    mail_subject = f'You successfully activated your account on {settings.PROJECT_NAME}.'
    message = render_to_string('accounts/email/success_activate.html', {
        'user': user,
        'domain': current_site.domain,
        'project_name': settings.PROJECT_NAME,
        'protocol': settings.HTTP_PROTOCOL
    })

    to_email = user.email

    send_mail(
        subject=mail_subject,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
        message=message,
        fail_silently=True,
    )


def send_activate_email(request, user):
    """ Send email to user after registrations to confirm account """

    current_site = get_current_site(request)
    mail_subject = f'Activate your account on {settings.PROJECT_NAME}.'
    message = render_to_string('accounts/email/activate.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'project_name': settings.PROJECT_NAME,
        'protocol': settings.HTTP_PROTOCOL
    })

    to_email = user.email

    send_mail(
        subject=mail_subject,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
        message=message,
        fail_silently=True,
    )
