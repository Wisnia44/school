from rest_framework import permissions

class CoursePermission(permissions.BasePermission):

	def has_permission(self, request, view):
		if request.user.is_authenticated:
			if request.user.is_teacher or request.user.is_principal:
				return True
			if request.user.is_student and request.method in permissions.SAFE_METHODS:
				return True
		return False

class GradePermission(permissions.BasePermission):

	def has_permission(self, request, view):
		if request.user.is_authenticated:
			if request.user.is_teacher or request.user.is_principal:
				return True
			if request.user.is_student and request.method in permissions.SAFE_METHODS:
				return True
		return False

class ForumPostPermission(permissions.BasePermission):

	def has_obj_permission(self, request, view, obj):
		if request.user.is_authenticated:
			if request.user.is_principal:
				return True
			if request.user == obj.author:
				return True
			if request.method == 'GET':
				return True
		return False

class CommentPermission(permissions.BasePermission):

	def has_obj_permission(self, request, view, obj):
		if request.user.is_authenticated:
			if request.user.is_principal:
				return True
			if request.user == obj.author:
				return True
			if request.method == 'GET':
				return True
		return False

class MessagePermission(permissions.BasePermission):

	def has_permission(self, request, view):
		if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
			return True
		return False
