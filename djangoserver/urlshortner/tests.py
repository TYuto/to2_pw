from django.test import TestCase
from .views import urls
from .models import Url, Domain
from unittest import mock
# Create your tests here.

def dummy_return_true(token, action):
    return True

def dummy_return_false(token, action):
    return False
class shortenUrlGenerateCase(TestCase):
    correct_parameter = { 'original' : 'https://test.com/', 'period': 'hour', 'recaptcha': 'hello' , 'domain_id': 1}
    def setUp(self):
        self.domain = Domain(host='localhost:3000/', enable_hours=True, enable_week=True, enable_month=False)
        self.domain.save()
        self.correct_parameter['domain_id'] = self.domain.pk
    def tearDown(self):
        Url.objects.all().delete()
        Domain.objects.all().delete()

    @mock.patch('urlshortner.views._verifyRecaptcha', dummy_return_true)
    def test_create_shortend_url(self):
        """
        正常に作成される
        """
        result = self.client.post('/api/urls/', self.correct_parameter)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(Url.objects.filter(shorten_url=result.json()['shorten_url']).count(), 1)

    @mock.patch('urlshortner.views._verifyRecaptcha', dummy_return_true)
    def test_incorrect_request(self):
        """
        不正なパラメータのリクエスト
        """
        result = self.client.post('/api/urls/', { 'hoge' : 'incorrect' })
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.content, b'parameter doesnt mach')

    @mock.patch('urlshortner.views._verifyRecaptcha', dummy_return_false)
    def test_not_auth_recaptcha(self):
        """
        recaptcha認証に失敗
        """
        result = self.client.post('/api/urls/', self.correct_parameter)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()['message'], 'reCAPTCHA認証に失敗しました')

    @mock.patch('urlshortner.views._verifyRecaptcha', dummy_return_true)
    def test_issue_limit(self):
        for i in range(5):
            r = self.client.post('/api/urls/', self.correct_parameter)
            self.assertTrue(r.json()['status'])
        r = self.client.post('/api/urls/', self.correct_parameter)
 
    @mock.patch('urlshortner.views._verifyRecaptcha', dummy_return_true)
    def test_invalid_domain(self):
        param = self.correct_parameter.copy()
        param['domain_id'] += 1
        result = self.client.post('/api/urls/', param)
        self.assertEqual(result.status_code, 404)

    @mock.patch('urlshortner.views._verifyRecaptcha', dummy_return_true)
    def test_invalid_period(self):
        param = self.correct_parameter.copy()
        param['period'] = 'month' 
        result = self.client.post('/api/urls/', param)
        self.assertEqual(result.status_code, 500)


    def test_generate_specified_length_str(self):
        for i in range(5):
            m = urls()
            result = m._createUrl(self.domain, i).split('/')[1]
            self.assertEqual(i, len(result))