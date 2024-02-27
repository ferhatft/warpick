
import os
import uuid
from django.dispatch import receiver

from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

STATUS = (
    ('new', 'New'),
    ('read', 'Read'),
    ('closed', 'Closed'),
)


# SUBJECT = (
#     ('teklif almak istiyorum', 'Teklif almak istiyorum'),
#     ('bilgi almak istiyorum ', 'Bilgi almak istiyorum '),
#     ('tanışma toplantısı talep ediyorum ', 'Tanışma toplantısı talep ediyorum '),
# )



class Contact(models.Model):
    # subject = models.CharField(max_length=500, choices=SUBJECT,default='teklif almak istiyorum')
    status = models.CharField(max_length=6, choices=STATUS, default='new')
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=3010,blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'


