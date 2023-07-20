from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageFilter
from django.utils import timezone
from django.conf import settings
from django.urls import reverse


GENDER_CHOICES = (
    ('Мужчина', 'МУЖЧИНА'),
    ('Женщина', 'ЖЕНЩИНА')
)


# Создать модель участников. У участника должна быть аватарка, пол, имя и фамилия, почта.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200, db_index=True,)
    lastname = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default='Мужчина')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    image2 = models.ImageField(default='default2.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        img.load()
        logo = Image.open(self.image2.path)
        logo.load()

        img_logo = logo.convert("L")
        threshold = 50
        img_logo = img_logo.point(lambda x: 255 if x > threshold else 0)
        img_logo = img_logo.resize(
            (img_logo.width // 5, img_logo.height // 5)
        )
        img_logo = img_logo.filter(ImageFilter.CONTOUR)
        img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)

        img.paste(img_logo, (0, 0), img_logo)
        img.save(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Friendship(models.Model):
    from_friend = models.ForeignKey(Profile, blank=True, on_delete=models.CASCADE, related_name="from_friends",)
    to_friend = models.ForeignKey(Profile, blank=True,on_delete=models.CASCADE,related_name="friends",)


    # def save(self, *args, **kwargs):
    #     super(Friendship, self).save(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     super(Friendship, self).save(*args, **kwargs)
    #
    # def get_absolute_url(self):
    #     return reverse('match', kwargs={'pk': self.pk})