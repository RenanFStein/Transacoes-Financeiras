
import os

from django.core.wsgi import get_wsgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alura.settings')

application = Cling(get_wsgi_application())
