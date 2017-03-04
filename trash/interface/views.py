from .models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

class IndexView(generic.TemplateView):
	template_name = 'interface/user_form.html'

class  DetailView(generic.TemplateView):
	template_name = "interface/sign_up.html"

class UserCreate(CreateView):
	model = User
	fields = ['email', 'model_name', 'model_number', 'size']

