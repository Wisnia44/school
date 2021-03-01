from rest_framework import serializers
from courses.models import Course, Grade, ForumPost, Comment

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Grade
		fields = '__all__'

class ForumPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = ForumPost
		fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
