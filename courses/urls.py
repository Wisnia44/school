from django.urls import path, include
from .views import (
	#Comment views
	CommentCreateView,
	CommentDeleteView,
	CommentDetailView,
	CommentUpdateView,
	#Courses views
	CourseCreateView,
	CourseDeleteView,
	CourseDetailView,
	CourseUpdateView,
	CoursesListView,
	#Grades Views
	GradeCreateView,
	GradeDeleteView,
	GradeDetailView,
	GradeUpdateView,
	GradesListView,
	#ForumPosts views
	ForumPostCreateView,
	ForumPostDeleteView,
	ForumPostDetailView,
	ForumPostsListView,
	)

urlpatterns = [
	#Comment views
	path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
	path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
	path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
	#Courses views
	path('course/create/', CourseCreateView.as_view(), name='course-create'),
	path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
	path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
	path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
	path('course/<int:pk>/grade/create/', GradeCreateView.as_view(), name='grade-create'),
	path('course/<int:pk>/grades/', GradesListView.as_view(), name='grades'),
	path('course/<int:pk>/forumposts/', ForumPostsListView.as_view(), name='forumposts'),
	path('course/<int:pk>/forumpost/create/', ForumPostCreateView.as_view(), name='forumpost-create'),
	path('courses', CoursesListView.as_view(), name='courses-list'),
	#Grades views
	path('grade/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade-delete'),
	path('grade/<int:pk>/', GradeDetailView.as_view(), name='grade-detail'),
	path('grade/<int:pk>/update/', GradeUpdateView.as_view(), name='grade-update'),
	#ForumPosts views
	path('forumpost/<int:pk>/delete/', ForumPostDeleteView.as_view(), name='forumpost-delete'),
	path('forumpost/<int:pk>/', ForumPostDetailView.as_view(), name='forumpost-detail'),
	path('forumpost/<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment-create'),
]
