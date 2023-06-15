import os
import time
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(20)
    print("hello")
