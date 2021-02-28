from rest_framework import serializers
from courses.models import Course, Grade

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = [
			'name',
			'teacher',
			'students',
		]

class GradeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Grade
		fields = [
			'grade',
			'course',
			'student',
			'teacher',
			'datetime',
		]
