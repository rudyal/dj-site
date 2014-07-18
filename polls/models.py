from django.db import models
import datetime
from django.utils import timezone
from tastypie.utils.timezone import now
from taggit.managers import TaggableManager

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

class PictureObject(models.Model):
	title = models.CharField(max_length=200)
	source = models.CharField(max_length=400)
	text = models.CharField(max_length=10000)
	tags1 = models.CharField(max_length=1000)
	gender = models.CharField(max_length=10)
	date = models.DateTimeField('date published')
	picture = models.FileField(upload_to='media')
	tags = TaggableManager()
	
	def __str__(self):
		return self.title
