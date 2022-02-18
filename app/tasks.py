from celery import shared_task


def django_setup():
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()


@shared_task
def compress(record_id):
    django_setup()
    from app.models import Record
    print('got', Record.objects.get(id=record_id).name_of_fish)
