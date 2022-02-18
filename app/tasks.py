from celery import shared_task
from wand.image import Image


def django_setup():
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()


@shared_task
def compress(record_id):
    django_setup()
    from app.models import Record
    record = Record.objects.get(id=record_id)
    image = Image(filename=record.photo.path)
    print("Original image size: {}".format(image.size))
    if image.width > 140 or image.height > 140:
        image.resize(140, 140)
        print("Resized image size: {}".format(image.size))
    image.save(filename=record.photo.path)

