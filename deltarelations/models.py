from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DeltaUser(models.Model):
  user = models.OneToOneField(User)
  birthdate = models.DateField()
  ethnicity = models.CharField(max_length=30)
  religion = models.CharField(max_length=30)
  relstat = models.CharField(max_length=30)
  sex = models.CharField(max_length=30)
  gender = models.CharField(max_length=30)
  location = models.CharField(max_length=30)

class Issues(models.Model):
  issue = models.CharField(max_length=30)

class Provided(models.Model):
  Uid1 = models.ForeignKey(DeltaUser, related_name="uid1")
  Uid2 = models.ForeignKey(DeltaUser, related_name="uid2")
  Iid = models.ForeignKey(Issues)

from django.core.exceptions import ValidationError

def validate_ratings(value):
  if (value < 0) or (value > 10):
    raise ValidationError('%s is not between 1 and 10' % value)

class Ratings(models.Model):
  rating = models.IntegerField(validators = [validate_ratings])

class Matches(models.Model):
  provider = models.ForeignKey(DeltaUser, related_name="provider")
  recipient = models.ForeignKey(DeltaUser, related_name="recipient")
  ratings = models.ForeignKey(Ratings)
  issue = models.ForeignKey(Issues)

