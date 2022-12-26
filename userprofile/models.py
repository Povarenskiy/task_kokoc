from django.db import models
from users.models import User
from colorfield.fields import ColorField

from questionnaire.models import Test

class Profile(models.Model):
    reward = models.IntegerField(default=0, verbose_name='Награда пользователя')
    background_color = ColorField(default='#FFFFFF', verbose_name='Цвет фона')
    border_color = ColorField(default='#FFFFFF', verbose_name='Цвет рамки')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tests = models.ManyToManyField(Test, blank=True)

    def __str__(self):
        return f'Профиль пользователя {self.user}'

