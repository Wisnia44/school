from django.urls import path
from .views import (
	MessageCreateView, 
	MessageReplyCreateView, 
	MessageDetailView, 
	MessagesReceivedListView,
	MessagesSentListView,
	)

urlpatterns = [
	path('message/create/', MessageCreateView.as_view(), name="message-create"),
	path('message/<int:pk>/create/', MessageReplyCreateView.as_view(), name="message-reply-create"),
	path('message/<int:pk>/', MessageDetailView.as_view(), name="message-detail"),
	path('messages/received/', MessagesReceivedListView.as_view(), name='messages-received'),
	path('messages/sent/', MessagesSentListView.as_view(), name='messages-sent'),

]
