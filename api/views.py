from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import CourseSerializer, GradeSerializer, ForumPostSerializer
from .permissions import CoursePermission, GradePermission, ForumPostPermission
from courses.models import Course, Grade, ForumPost

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [CoursePermission]
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_teacher or self.request.user.is_principal:
            return Course.objects.all()
        elif self.request.user.is_student:
            return Course.objects.filter(students__id=self.request.user.pk)
        else:
            return Course.objects.none()

class GradeViewSet(viewsets.ModelViewSet):
    permission_classes = [GradePermission]
    serializer_class = GradeSerializer

    def get_queryset(self):
        if self.request.user.is_principal:
            return Grade.objects.all()
        if self.request.user.is_teacher:
            return Grade.objects.filter(teacher=self.request.user)
        elif self.request.user.is_student:
            return Grade.objects.filter(student=self.request.user)
        else:
            return Grade.objects.none()

class ForumPostViewSet(viewsets.ModelViewSet):
    permission_classes = [ForumPostPermission]
    serializer_class = ForumPostSerializer

    def get_queryset(self):
        if self.request.user.is_principal:
            return ForumPost.objects.all()
        if self.request.user.is_teacher:
            return ForumPost.objects.filter(course__teacher=self.request.user)
        if self.request.user.is_student:
            return ForumPost.objects.filter(course__students__id=self.request.user.pk)
        else:
            return ForumPost.objects.none()
