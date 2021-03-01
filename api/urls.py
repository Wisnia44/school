from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import CourseViewSet, GradeViewSet, ForumPostViewSet, CommentViewSet, MessageViewSet

schema_view = get_schema_view(
	openapi.Info(
		title="Docs School",
		default_version='v1',
		description="School Documentation",
		terms_of_service="",
		contact=openapi.Contact(email="school.maintaining.app@gmail.com"),
		license=openapi.License(name="BSD License"),
		),
	public=True,
	permission_classes=[permissions.AllowAny],
	)

router = DefaultRouter()
router.register(r'courses', CourseViewSet, 'courses-api')
router.register(r'grades', GradeViewSet, 'grades-api')
router.register(r'posts', ForumPostViewSet, 'posts-api')
router.register(r'comments', CommentViewSet, 'comments-api')
router.register(r'messages', MessageViewSet, 'messages-api')

urlpatterns = [
	path('token/', obtain_auth_token, name='token'),
	url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	path('', include(router.urls)),
]
