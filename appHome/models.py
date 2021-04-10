from django.db import models

# User properties
class User(models.Model):
	# Finite list of choices for gender
	# List of tuples, (db_value, display_value)
	GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	birthdate = models.DateField(blank=True)
	bio = models.TextField()
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
	subscribed = models.ManyToManyField('Subscription', blank=True)

# Subscription (category) properties
class Subscription(models.Model):
	name = models.CharField(max_length=50)