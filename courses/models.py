from django.db import models
from administration.models import User
from django.urls import reverse

class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, related_name='teacher', on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(User, related_name='students')
    
    def get_absolute_url(self):
    	return reverse('course-detail', args=[str(self.pk)])

class Grade(models.Model):
	grade = models.CharField(max_length=1)
	course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
	student = models.ForeignKey(User, related_name='student', on_delete=models.DO_NOTHING)
	teacher = models.ForeignKey(User, related_name='teacher_grading', on_delete=models.DO_NOTHING)
	datetime = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('grade-detail', args=[str(self.pk)])

class ForumPost(models.Model):
	topic = models.CharField(max_length=25)
	content = models.CharField(max_length=500)
	datetime = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

	def get_absolute_url(self):
		return reverse('forumpost-detail', args=[str(self.pk)])

class Comment(models.Model):
	content = models.CharField(max_length=300)
	datetime = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	forumpost = models.ForeignKey(ForumPost, on_delete=models.DO_NOTHING)

	def get_absolute_url(self):
		return reverse('comment-detail', args=[str(self.pk)])
