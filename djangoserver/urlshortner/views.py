from .models import Url
from rest_framework.views import APIView
from django.http import HttpResponse
import json
import uuid
from datetime import datetime, timedelta, timezone
import random
from django.contrib.auth.models import User
class urls(APIView):
    def get(self, request):
        now = datetime.now()
        if request.user.is_authenticated:
            urls = Url.objects.filter(user=request.user.id).order_by('-updated_at')
        else:
            try:
                pk = request.session['uuid']
            except KeyError:
                pk = str(uuid.uuid4())
                request.session['uuid'] = pk
            urls = Url.objects.filter(tempuser_id=pk).order_by('-updated_at')
        data = [
            {
                'original_url': url.original_url,
                'shorten_url': url.shorten_url,
                'validity_period': url.validity_period,
                'expiration_date': url.expiration_date.timestamp(),
                'until': (url.expiration_date.timestamp()-now.timestamp())*100/url.validity_period
            } for url in urls]
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
        return response
    def post(self, request):
        try:
            original_url = request.data['original']
            period = request.data['period']
        except KeyError:
            return HttpResponse('parameter doesn mach',status=500)
        print(request.user)
        if request.user.is_authenticated:
            url = Url(user=User.objects.get(id=request.user.id))
            urllen = 0
        else:
            print('hoge')
            try:
                pk = request.session['uuid']
            except KeyError:
                pk = str(uuid.uuid4())
                request.session['uuid'] = pk
            url = Url(tempuser_id=pk)
            urllen = 1
        now = datetime.now()
        url.original_url = original_url
        if period == 'hour':
            url.validity_period = 3600
            urllen +=2
            period = timedelta(hours=3)
        elif period ==  'days':
            url.validity_period = 43200
            urllen += 3
            period = timedelta(days=5)
        elif period ==  'month':
            url.validity_period = 12960000
            urllen += 4
            period = timedelta(days=150)
        else:
            return HttpResponse('faild',status=500)
        url.expiration_date = now + period
        data = {'shorten_url': self._saveUrl(url, urllen)}
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
        return response
    def _createUrl(self,urllen):
        domains = [
            '22ur.tk/',
            '22ur.cf/',
        ]
        ranstr = 'abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789'
        return random.choice(domains) + ''.join([random.choice(ranstr) for i in range(urllen)])
    def _saveUrl(self,url,urllen):
        url.shorten_url = self._createUrl(urllen)
        try:
            url.save()
            return url.shorten_url
        except:
            conflict_url = Url.objects.get(shorten_url=url.shorten_url)
            if conflict_url.expiration_date < datetime.now(tz=timezone.utc):
                conflict_url.original_url = url.original_url
                conflict_url.expiration_date = url.expiration_date
                conflict_url.user = url.user
                conflict_url.tempuser_id = url.tempuser_id
                conflict_url.validity_period = url.validity_period
                conflict_url.save()
                return url.shorten_url
            url.shorten_url = self._createUrl(urllen)
            self._saveUrl(url, urllen)