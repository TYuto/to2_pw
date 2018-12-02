from .models import Url
from rest_framework.views import APIView
from django.http import HttpResponse
import json
import uuid
from datetime import datetime, timedelta, timezone
import random
from django.contrib.auth.models import User
from django.shortcuts import redirect
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
            } for url in urls if url.expiration_date.timestamp() > now.timestamp()]
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
        return response
    def post(self, request):
        now = datetime.now()
        try:
            original_url = request.data['original']
            period = request.data['period']
        except KeyError:
            return HttpResponse('parameter doesn mach',status=500)
        if request.user.is_authenticated:
            url = Url(user=User.objects.get(id=request.user.id))
            urllen = 0
            if  Url.objects.filter(expiration_date__gt = now,user=request.user.id).count() >= 20:
                data = {'status': False,'message': '一度に生成できる短縮URLは20個までです'}
                json_str = json.dumps(data, ensure_ascii=False, indent=2)
                response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
                return response
        else:
            try:
                pk = request.session['uuid']
            except KeyError:
                pk = str(uuid.uuid4())
                request.session['uuid'] = pk
            url = Url(tempuser_id=pk)
            urllen = 1
            if  Url.objects.filter(expiration_date__gt = now,user=request.user.id).count() >= 5:
                data = {'status': False,'message': '一度に生成できる短縮URLは5個までです、ログインすると制限を20個まで増やすことができます'}
                json_str = json.dumps(data, ensure_ascii=False, indent=2)
                response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
                return response
        url.original_url = original_url
        if period == 'hour':
            url.validity_period = 60*60*3
            urllen +=2
            period = timedelta(hours=3)
        elif period ==  'days':
            url.validity_period = 60*60*24*5
            urllen += 3
            period = timedelta(days=5)
        elif period ==  'month':
            url.validity_period = 60*60*24*150
            urllen += 4
            period = timedelta(days=150)
        else:
            return HttpResponse('faild',status=500)
        url.expiration_date = now + period
        data = {'status':True,'shorten_url': self._saveUrl(url, urllen)}
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
        return response
    def _createUrl(self,urllen):
        domains = [
            'red.localhost/',
        ]
        ranstr = 'abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789'
        return random.choice(domains) + ''.join([random.choice(ranstr) for i in range(urllen)])
    def _saveUrl(self,url,urllen):
        now = datetime.now()
        url.shorten_url = self._createUrl(urllen)
        try:
            oldurl = Url.objects.filter(expiration_date__gt = now).get(shorten_url = url.shorten_url)
            if oldurl.expiration_date.timestamp() > now.timestamp():
                return self._saveUrl(url,urllen)
        except Url.DoesNotExist:
            url.save()
        url.save()
        return url.shorten_url
def redirectView(request, domain='', rand=''):
    now = datetime.now()
    try:
        url = Url.objects.filter(expiration_date__gt = now).get(shorten_url=domain+'/'+rand)
        return redirect(url.original_url)
    except:
        return redirect('/')
def getuser(request):
    if request.user.is_authenticated:
        data = {'authed': True,'username': request.user.username}
    else:
        data = {'authed': False}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
    return response