from django.db import models

# Create your models here.
class Event (models.Model):
	title 		= models.CharField(max_length=100)
	description 	= models.TextField()
	date 		= models.DateField()
	time 		= models.TimeField()
	location 	= models.CharField(max_length=100)
	category 	= models.CharField(max_length=50)
	
	def __str__(self):
		return self.title

class Attendee (models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	event = models.ForeignKey('Event', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.event.title}"
	