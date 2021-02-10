from django.contrib import admin
from .models import Course, Grade, ForumPost, ForumPostComment

# Register your models here.
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(ForumPost)
admin.site.register(ForumPostComment)
