from django.conf import settings
from django.shortcuts import redirect

REDIRECT_URI = f'http://{settings.ELK_SETTINGS.kibana_host}:5601/app/logs/stream'


def redirect2kibana(request):
    return redirect(REDIRECT_URI)
