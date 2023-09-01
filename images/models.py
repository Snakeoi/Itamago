import os
from django.db import models
from django.conf import settings
from PIL import Image as PilImage


class Image(models.Model):
    file = models.ImageField(upload_to='static/uploads/%Y-%m-%d', null=False)

    @property
    def filename(self):
        return self.file.name.split('/')[-1]

    @property
    def folder(self):
        return self.file.name.replace(self.filename, '')

    @property
    def thumbnail_uri(self):
        return f"{settings.SITE_DOMAIN}/{self.folder}/thumbnail_{self.filename}"

    @property
    def main_image_uri(self):
        return f"{settings.SITE_DOMAIN}/{self.folder}/{self.filename}"

    def __repr__(self):
        return self.file.name

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.file:
            img = PilImage.open(self.file.path)
            thumbnail_img = img.copy()

            width, height = thumbnail_img.size
            current_ratio = width / height

            desired_ratio = 1/1
            desired_dimension = 300

            if current_ratio != desired_ratio:
                if current_ratio > desired_ratio:
                    new_width = int(height * desired_ratio)
                    left = int((width - new_width) / 2)
                    right = int((width + new_width) / 2)
                    box = (left, 0, right, height)
                else:
                    new_height = int(width / desired_ratio)
                    top = int((height - new_height) / 2)
                    bottom = int((height + new_height) / 2)
                    box = (0, top, width, bottom)

                thumbnail_img = thumbnail_img.crop(box)

            if thumbnail_img.size[0] > desired_dimension or thumbnail_img.size[1] > desired_dimension:
                thumbnail_img.thumbnail((desired_dimension, desired_dimension), PilImage.ANTIALIAS)

            thumbnail_path, thumbnail_filename = os.path.split(self.file.name)
            thumbnail_filename = "thumbnail_" + thumbnail_filename
            thumbnail_file_path = os.path.join(thumbnail_path, thumbnail_filename)

            thumbnail_img.save(thumbnail_file_path)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)

            thumbnail_path, thumbnail_filename = os.path.split(self.file.path)
            thumbnail_filename = "thumbnail_" + thumbnail_filename
            thumbnail_file_path = os.path.join(thumbnail_path, thumbnail_filename)
            if os.path.isfile(thumbnail_file_path):
                os.remove(thumbnail_file_path)
