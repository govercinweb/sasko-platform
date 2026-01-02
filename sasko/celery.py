import os

from celery import Celery
from celery.signals import task_failure

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sasko.settings')

app = Celery('sasko')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# @task_failure.connect()
# def celery_mail_admins(**kwargs):
#     from django.core.mail import mail_admins
#     import socket
#     from django.conf import settings
#     if settings.DEBUG:
#         return
#     """ celery 4.0 onward has no method to send emails on failed tasks
#         so this event handler is intended to replace it
#         """
#     subject = "[Django][{queue_name}@{host}] Error: Task {sender.name} ({task_id}): {exception}".format(
#         queue_name="celery",  # `sender.queue` doesn't exist in 4.1?
#         host=socket.gethostname(),
#         **kwargs
#     )
#     message = """Task {sender.name} with id {task_id} raised exception:
#     -------------------------
#     {exception!r}
#     -------------------------
#     Task was called with args: {args} kwargs: {kwargs}.
#     -------------------------
#     The contents of the full traceback was:
#     -------------------------
#     {einfo}
#         """.format(
#         **kwargs
#     )
#     mail_admins(subject, message)
