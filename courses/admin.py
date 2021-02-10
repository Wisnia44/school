from django.contrib import admin
from .models import Course, Grade, ForumPost, Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(ForumPost)
