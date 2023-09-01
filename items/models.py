from django.db import models
from images.models import Image
from django.conf import settings


class Item(models.Model):
    name = models.CharField(max_length=64, null=False)
    serial_number = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    main_image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='main_image'
    )
    item_images = models.ManyToManyField(
        Image,
        blank=True,
        related_name='item_images'
    )

    @property
    def thumbnail_uri(self):
        if self.main_image is not None:
            return self.main_image.thumbnail_uri
        else:
            return settings.SITE_DOMAIN + '/static/images/no_photo.jpg'

    @property
    def main_image_uri(self):
        if self.main_image is not None:
            return self.main_image.main_image_uri
        else:
            return settings.SITE_DOMAIN + '/static/images/no_photo.jpg'