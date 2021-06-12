from django.db import models
from django.urls import reverse

class Comment(models.Model):
    text = models.TextField(default = '', blank = True, null = False, verbose_name = 'Комментарий:')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
