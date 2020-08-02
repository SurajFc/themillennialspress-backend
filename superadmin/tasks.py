from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from users.models import User

email_from = settings.EMAIL_HOST_USER


@shared_task(name="Send OTP Mail")
def sentOTP(email, otp):

    message = f' Your OTP is : ' + otp
    recipient_list = [email]

    send_mail(
        "OTP",
        message,
        email_from,
        recipient_list,
        fail_silently=False,
    )
    return None


@shared_task(name="Send New Password Mail")
def sentPassword(email, password):
    message = f' Your New Password is : ' + password
    recipient_list = [email]

    send_mail(
        "New Password ",
        message,
        email_from,
        recipient_list,
        fail_silently=False,
    )
    return None
