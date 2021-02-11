from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import User

# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
	model = User
	template_name = 'administration/user_detail.html'

	def get_object(self):
		return self.request.user
