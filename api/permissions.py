from rest_framework import permissions

class CoursePermission(permissions.BasePermission):

	def has_permission(self, request, view):
		if request.user.is_authenticated:
			if request.user.is_teacher or request.user.is_principal:
				return True
			if request.user.is_student and request.method in permissions.SAFE_METHODS:
				return True
		return False
