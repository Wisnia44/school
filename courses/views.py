from django.shortcuts import render, reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Course, Grade, ForumPost, Comment
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin

def teacher_check(user):
    return user.is_teacher

#Courses views
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(teacher_check), name='dispatch')
class CourseCreateView(CreateView):
	model = Course
	template_name = 'courses/course_create.html' 
	fields = ['name', 'teacher', 'students']

	def get_form_kwargs(self,*args,**kwargs):
		kwargs = super(CourseCreateView, self).get_form_kwargs(*args,**kwargs)
		return kwargs

	def get_success_url(self,*args,**kwargs):
		return reverse('course-detail', kwargs={'pk':self.object.pk})

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(teacher_check), name='dispatch')
class CourseDeleteView(DeleteView):
	model = Course
	template_name = 'courses/course_delete.html'

	def get_success_url(self):
		return reverse('courses-list')

@method_decorator(login_required, name='dispatch')
class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/course_detail.html'

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(teacher_check), name='dispatch')
class CourseUpdateView(UpdateView):
	model = Course
	template_name = 'courses/course_update.html' 
	fields = ['name', 'teacher', 'students']

	def get_form_kwargs(self,*args,**kwargs):
		kwargs = super(CourseUpdateView, self).get_form_kwargs(*args,**kwargs)
		return kwargs

	def get_success_url(self,*args,**kwargs):
		return reverse('course-detail', kwargs={'pk':self.object.pk})

@method_decorator(login_required, name='dispatch')
class CoursesListView(ListView):
	model = Course
	template_name = 'courses/courses_list.html'
	context_object_name = 'courses'

	def get_queryset(self):
		queryset = super(CoursesListView, self).get_queryset()
		if self.request.user.teacher==True:
			queryset = Course.objects.filter(teacher=self.request.user)
			print("jkhbfsjhbgiueuh",queryset)
		elif self.request.user.student==True:
			queryset = Course.object.filter(students__id=self.request.user.pk)
			print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx", queryset)
		return queryset

#Grades views
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(teacher_check), name='dispatch')
class GradeCreateView(CreateView):
	model = Grade
	template_name = 'courses/grade_create.html' 
	fields = ['grade', 'student']

	def get_form_kwargs(self,*args,**kwargs):
		kwargs = super(GradeCreateView, self).get_form_kwargs(*args,**kwargs)
		if kwargs['instance'] is None:
			kwargs['instance'] = Grade()
		kwargs['instance'].teacher = self.request.user
		kwargs['instance'].course = Course.objects.get(pk=self.kwargs.get('pk'))
		return kwargs

	def get_success_url(self,*args,**kwargs):
		return reverse('grade-detail', kwargs={'pk':self.object.pk})

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(teacher_check), name='dispatch')
class GradeDeleteView(DeleteView):
	model = Grade
	template_name = 'courses/grade_delete.html'

	def get_success_url(self,*args,**kwargs):
		return reverse('grades', kwargs={'pk':self.object.course.pk})

@method_decorator(login_required, name='dispatch')
class GradeDetailView(DetailView):
	model = Grade
	template_name = 'courses/grade_detail.html'

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(teacher_check), name='dispatch')
class GradeUpdateView(UpdateView):
	model = Grade
	template_name = 'courses/grade_update.html' 
	fields = ['grade', 'course', 'student']

	def get_success_url(self,*args,**kwargs):
		return reverse('grade-detail', kwargs={'pk':self.object.pk})

@method_decorator(login_required, name='dispatch')
class GradesListView(ListView):
	model = Grade
	template_name = 'courses/course_grades.html'
	context_object_name = 'grades'

	def get_queryset(self,*args,**kwargs):
		queryset = super(GradesListView, self).get_queryset()
		queryset = queryset.filter(course=self.kwargs['pk'])
		return queryset

#ForumPosts views
@method_decorator(login_required, name='dispatch')
class ForumPostCreateView(CreateView):
	model = ForumPost
	template_name = 'courses/forumpost_create.html' 
	fields = ['topic', 'content']

	def get_form_kwargs(self,*args,**kwargs):
		kwargs = super(ForumPostCreateView, self).get_form_kwargs(*args,**kwargs)
		if kwargs['instance'] is None:
			kwargs['instance'] = ForumPost()
		kwargs['instance'].author = self.request.user
		kwargs['instance'].course = Course.objects.get(pk=self.kwargs.get('pk'))
		return kwargs

	def get_success_url(self,*args,**kwargs):
		return reverse('forumpost-detail', kwargs={'pk':self.object.pk})

@method_decorator(login_required, name='dispatch')
class ForumPostDeleteView(UserPassesTestMixin, DeleteView):
	model = ForumPost
	template_name = 'courses/forumpost_delete.html'

	def get_form_kwargs(self,*args,**kwargs):
		kwargs = super(CourseUpdateView, self).get_form_kwargs(*args,**kwargs)
		return kwargs

	def get_success_url(self,*args,**kwargs):
		return reverse('forumposts', kwargs={'pk':self.object.course.pk})

	def test_func(self, *args, **kwargs):
		post = ForumPost.objects.get(pk=self.kwargs.get('pk'))
		if self.request.user == post.author:
			return True
		return False

@method_decorator(login_required, name='dispatch')
class ForumPostDetailView(DetailView):
	model = ForumPost
	template_name = 'courses/forumpost_detail.html'

@method_decorator(login_required, name='dispatch')
class ForumPostUpdateView(UserPassesTestMixin, UpdateView):
	model = ForumPost
	template_name = 'courses/forumpost_update.html' 
	fields = ['topic', 'content']

	def get_success_url(self,*args,**kwargs):
		return reverse('forumpost-detail', kwargs={'pk':self.object.pk})

	def test_func(self, *args, **kwargs):
		post = ForumPost.objects.get(pk=self.kwargs.get('pk'))
		if self.request.user == post.author:
			return True
		return False

@method_decorator(login_required, name='dispatch')
class ForumPostsListView(ListView):
	model = ForumPost
	template_name = 'courses/course_forumposts.html'
	context_object_name = 'forumposts'

	def get_queryset(self,*args,**kwargs):
		queryset = super(ForumPostsListView, self).get_queryset()
		queryset = queryset.filter(course=self.kwargs['pk'])
		return queryset

#Comment views
@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
	model = Comment
	template_name = 'courses/comment_create.html' 
	fields = ['content']

	def get_form_kwargs(self,*args,**kwargs):
		kwargs = super(CommentCreateView, self).get_form_kwargs(*args,**kwargs)
		if kwargs['instance'] is None:
			kwargs['instance'] = Comment()
		kwargs['instance'].author = self.request.user
		kwargs['instance'].forumpost = ForumPost.objects.get(pk=self.kwargs.get('pk'))
		return kwargs

	def get_success_url(self,*args,**kwargs):
		return reverse('comment-detail', kwargs={'pk':self.object.pk})

@method_decorator(login_required, name='dispatch')
class CommentDeleteView(UserPassesTestMixin, DeleteView):
	model = Comment
	template_name = 'courses/comment_delete.html'

	def get_success_url(self,*args,**kwargs):
		return reverse('forumpost-detail', kwargs={'pk':self.object.forumpost.pk})

	def test_func(self, *args, **kwargs):
		comment = Comment.objects.get(pk=self.kwargs.get('pk'))
		if self.request.user == comment.author:
			return True
		return False

@method_decorator(login_required, name='dispatch')
class CommentDetailView(DetailView):
	model = Comment
	template_name = 'courses/comment_detail.html'

@method_decorator(login_required, name='dispatch')
class CommentUpdateView(UserPassesTestMixin, UpdateView):
	model = Comment
	template_name = 'courses/comment_update.html' 
	fields = ['content']

	def get_success_url(self,*args,**kwargs):
		return reverse('comment-detail', kwargs={'pk':self.object.pk})

	def test_func(self, *args, **kwargs):
		comment = Comment.objects.get(pk=self.kwargs.get('pk'))
		if self.request.user == comment.author:
			return True
		return Falsee
