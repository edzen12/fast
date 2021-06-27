from django.conf import settings
from django.core.mail import EmailMessage

from frilance_1.celery import app


@app.task
def send_info(fullname: str, number: str):
    message = f"""
    ФИО: {fullname}
    Телефон: {number}
    """
    email = EmailMessage(
        "Форма обратной связи с сайта FastPrepUSA!",
        message, settings.EMAIL_HOST_USER,
        ['oichiev.edzen@gmail.com', 'office@fastprepusa.com'],
    )
    email.send(fail_silently=False)
