from django.shortcuts import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from .models import Message
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin

@method_decorator(login_required, name='dispatch')
class MessageCreateView(CreateView):
	model = Message
	template_name = 'message/message_create.html' 
	fields = ['receiver','topic','content']

	def get_form_kwargs(self,*args,**kwargs):
		kwargs = super(MessageCreateView, self).get_form_kwargs(*args,**kwargs)
		if kwargs['instance'] is None:
			kwargs['instance'] = Message()
		kwargs['instance'].author = self.request.user
		return kwargs

	def get_success_url(self,*args,**kwargs):
		return reverse('message-detail', kwargs={'pk':self.object.pk})

@method_decorator(login_required, name='dispatch')
class MessageReplyCreateView(UserPassesTestMixin,CreateView):
	model = Message
	template_name = 'message/message_reply_create.html' 
	fields = ['topic', 'content']

	def get_form_kwargs(self,*args,**kwargs):
		kwargs = super(MessageReplyCreateView, self).get_form_kwargs(*args,**kwargs)
		if kwargs['instance'] is None:
			kwargs['instance'] = Message()
		kwargs['instance'].author = self.request.user
		prev_message = Message.objects.get(pk=self.kwargs.get('pk'))
		kwargs['instance'].in_reply_to = prev_message
		kwargs['instance'].receiver = prev_message.author
		return kwargs

	def get_success_url(self,*args,**kwargs):
		return reverse('message-detail', kwargs={'pk':self.object.pk})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['prev_message'] = Message.objects.get(pk=self.kwargs.get('pk'))
		return context

	def test_func(self, *args, **kwargs):
		message = Message.objects.get(pk=self.kwargs.get('pk'))
		if self.request.user == message.receiver:
			return True
		return False

@method_decorator(login_required, name='dispatch')
class MessageDetailView(UserPassesTestMixin, DetailView):
	model = Message
	template_name = 'message/message_detail.html'

	def test_func(self, *args, **kwargs):
		message = Message.objects.get(pk=self.kwargs.get('pk'))
		if self.request.user == message.author or self.request.user == message.receiver:
			return True
		return False

@method_decorator(login_required, name='dispatch')
class MessagesReceivedListView(ListView):
	model = Message
	template_name = 'message/messages_list.html'
	context_object_name = 'messages'

	def get_queryset(self):
		queryset = Message.objects.filter(receiver=self.request.user)
		return queryset

@method_decorator(login_required, name='dispatch')
class MessagesSentListView(ListView):
	model = Message
	template_name = 'message/messages_list.html'
	context_object_name = 'messages'

	def get_queryset(self):
		queryset = Message.objects.filter(author=self.request.user)
		return queryset
