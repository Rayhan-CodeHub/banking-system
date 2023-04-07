
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'islamic_bank_limited.settings')

application = get_asgi_application()
