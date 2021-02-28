from rest_framework import serializers
from courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = [
			'name',
			'teacher',
			'students',
		]

	def get_url(self, obj):
		request = self.context.get("request")
		return obj.get_api_url(request=request)
