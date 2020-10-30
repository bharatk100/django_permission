from django.db import models
from django.contrib.auth.models import User
from PIL import Image


CHOICE_GENDER = [(1, 'Male'), (2, 'Female')]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=CHOICE_GENDER, default='1')
    image = models.ImageField(default='default.jpg', upload_to='media')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



