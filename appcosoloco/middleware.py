from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        static_path = urlparse(settings.STATIC_URL).path
        self.static_path = static_path if static_path.startswith('/') else f'/{static_path}'

    def __call__(self, request):
        is_login_page = request.path == reverse('login')
        is_static_file = request.path.startswith(self.static_path)

        if not request.user.is_authenticated and not (is_login_page or is_static_file):
            return redirect_to_login(request.get_full_path(), settings.LOGIN_URL)

        return self.get_response(request)
