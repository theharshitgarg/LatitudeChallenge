from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    fees = models.FloatField(default=0.0)
    max_limit = models.IntegerField(default=0)

# # Create your models here.
# class Venue(models.Model):
#     landmark = models.CharField(max_length=100)
#     lat = models.FloatField(default=0.0)
#     lng = models.FloatField(default=0.0)
#     event = models.ForeignKey(Event)


class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    id_card = models.ImageField(upload_to='id_cards')

    def __str__(self):
        return self.first_name+" "+self.last_name


class EventRegistration(models.Model):
    REGISTRATION_CHOICES = (
        ('SF', 'Self'),
        ('GR', 'Group'),
        ('CP', 'Corporate'),
        ('OR', 'Others')
    )
    event = models.ForeignKey(Event)
    participants = models.ManyToManyField(Participant)
    registration_date = models.DateTimeField(default=timezone.now)
    registration_type = models.CharField(max_length=2, choices=REGISTRATION_CHOICES,
                                        default='SF')
                                            
