from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class LoginAccessTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='jugador',
            password='UnaClaveSegura123!',
        )

    def test_login_page_is_public(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)

    def test_site_pages_require_login(self):
        protected_paths = [
            reverse(name)
            for name in ('inicio', 'historia', 'desarrollo', 'contacto')
        ] + ['/admin/']
        for path in protected_paths:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertRedirects(
                    response,
                    f'{reverse("login")}?next={path}',
                    fetch_redirect_response=False,
                )

    def test_login_returns_user_to_requested_page(self):
        response = self.client.post(
            f'{reverse("login")}?next={reverse("historia")}',
            {'username': self.user.username, 'password': 'UnaClaveSegura123!'},
        )

        self.assertRedirects(response, reverse('historia'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_authenticated_user_can_open_site_pages_and_log_out(self):
        self.client.force_login(self.user)

        for name in ('inicio', 'historia', 'desarrollo', 'contacto'):
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, 'Cerrar sesión')

    def test_invalid_credentials_do_not_authenticate(self):
        response = self.client.post(
            reverse('login'),
            {'username': self.user.username, 'password': 'incorrecta'},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Usuario o contraseña incorrectos')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_logout_ends_session(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('logout'))

        self.assertRedirects(response, reverse('login'))
        self.assertNotIn('_auth_user_id', self.client.session)
