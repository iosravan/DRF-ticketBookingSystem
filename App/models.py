from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Tickets(models.Model):
    movie_id = models.CharField(max_length=50,primary_key=True,default='M-1001')
    movie_name = models.CharField(max_length=50)
    total_tickets = models.IntegerField(default=1000)
    status = models.CharField(max_length=50)
    available = models.IntegerField(default=1000)
    Total = models.IntegerField(default=1000)
    createdDate = models.DateTimeField(default=timezone.now, editable=False)
    price = models.IntegerField(default=200)
    class Meta:
        verbose_name = 'Tickets'
        verbose_name_plural = 'Tickets details'

    def __str__(self):
        return self.movie_name

class ReservedTickets(models.Model):
    ticket_id = models.CharField(max_length=50,primary_key=True)
    Registered_user = models.CharField(max_length=50)
    movie_name = models.CharField(max_length=50)
    movie_id = models.CharField(max_length=50,default='M-0000')
    tickets_booked = models.IntegerField(default=1000)
    createdDate = models.DateTimeField(default=timezone.now, editable=False)
    price = models.IntegerField(default=400)
    class Meta:
        verbose_name = 'User Tickets'
        verbose_name_plural = 'User Tickets'

    def __str__(self):
        return self.ticket_id
