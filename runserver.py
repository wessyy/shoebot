import os

def runserver():
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
	from django.core.management import call_command
	from django.core.wsgi import get_wsgi_application 
	application = get_wsgi_application()
	call_command('runserver',  '127.0.0.1:8000')