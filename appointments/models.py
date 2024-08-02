from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} booked an appointment for the date:{self.date} at {self.time} for {self.description}. Email:{self.email}"