from django.db import models
from administration.models import User
from django.shortcuts import reverse

# Create your models here.
class Message(models.Model):
	topic = models.CharField(max_length=50)
	content = models.CharField(max_length=500)
	author = models.ForeignKey(User, related_name='author', on_delete=models.DO_NOTHING)
	receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.DO_NOTHING)
	in_reply_to = models.ForeignKey(
		'Message', 
		on_delete=models.DO_NOTHING, 
		null=True, 
		blank=True
		)

	def get_absolute_url(self):
		return reverse('message-detail', args=[str(self.pk)])
