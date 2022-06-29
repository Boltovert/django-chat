from django.db import models


class ChannelSidebar(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'Название чата')
    # content = models.TextField(verbose_name='Контент')