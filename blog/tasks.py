from celery import shared_task

from django.core.mail import send_mail


@shared_task
def notify(mas):
    from_email = 'site@gmail.com'
    subject = 'Notification'
    recipient_list = 'admin@admin.com'
    send_mail(subject, mas, from_email, [recipient_list])


@shared_task
def notify_user(mas, email):
    from_email = 'site@gmail.com'
    subject = 'Notification'
    recipient_list = email
    send_mail(subject, mas, from_email, [recipient_list])
