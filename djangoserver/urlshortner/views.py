from .models import Url, Domain
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import json
import os
import uuid
from datetime import datetime, timedelta, timezone
import random
from django.contrib.auth.models import User
from django.shortcuts import redirect
import urllib
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
            recaptcha_token = request.data['recaptcha']
            domain_id = request.data['domain_id']
        except KeyError:
            return HttpResponse('parameter doesnt mach',status=400)
        domain = get_object_or_404(Domain, pk=domain_id)


        if not _verifyRecaptcha(recaptcha_token, 'create'):
            data = {'status': False,'message': 'reCAPTCHA認証に失敗しました'}
            json_str = json.dumps(data, ensure_ascii=False, indent=2)
            return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
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
            if  Url.objects.filter(expiration_date__gt = now,tempuser_id=pk).count() >= 5:
                data = {'status': False,'message': '一度に生成できる短縮URLは5個までです、ログインすると制限を20個まで増やすことができます'}
                json_str = json.dumps(data, ensure_ascii=False, indent=2)
                response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=406)
                return response
        url.original_url = original_url
        if period == 'hour' and domain.enable_hours:
            url.validity_period = 60*60*3
            urllen +=2
            period = timedelta(hours=3)
        elif period ==  'days' and domain.enable_week:
            url.validity_period = 60*60*24*5
            urllen += 3
            period = timedelta(days=5)
        elif period ==  'month' and domain.enable_month:
            url.validity_period = 60*60*24*150
            urllen += 4
            period = timedelta(days=150)
        else:
            return HttpResponse('faild',status=500)
        url.expiration_date = now + period
        data = {'status':True,'shorten_url': self._saveUrl(url, domain, urllen)}
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
        return response
    def delete(self, request):
        try:
            shorten_url = request.data['shorten_url']
        except KeyError:
            return HttpResponse('parameter doesn mach',status=400)
        if request.user.is_authenticated:
            url = get_object_or_404(Url, shorten_url=shorten_url, user=request.user.id)
        else:
            try:
                pk = request.session['uuid']
            except KeyError:
                return HttpResponse('parameter doesn mach',status=400)
            url = get_object_or_404(Url, shorten_url=shorten_url, tempuser_id=pk)
        url.delete()
        return HttpResponse('', status=200)


    def _createUrl(self, domain,urllen):
        ranstr = 'abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789'
        return domain.host + ''.join([random.choice(ranstr) for i in range(urllen)])
    def _saveUrl(self,url, domain, urllen):
        now = datetime.now()
        url.shorten_url = self._createUrl(domain, urllen)
        try:
            oldurl = Url.objects.filter(expiration_date__gt = now).get(shorten_url = url.shorten_url)
            if oldurl.expiration_date.timestamp() > now.timestamp():
                return self._saveUrll(url,domain, urllen)
        except Url.DoesNotExist:
            url.save()
        url.save()
        return url.shorten_url
def redirectView(request, rand=''):
    domain = request.get_host()
    now = datetime.now()
    try:
        url = Url.objects.filter(expiration_date__gt = now).get(shorten_url=domain+'/'+rand)
        return redirect(url.original_url)
    except:
        # return redirect('https://to2.pw/p/404?url=''https://' + domain + '/' + rand)
        return redirect('http://localhost:3000/404?url=''https://' + domain + '/' + rand)
def getuser(request):
    if request.user.is_authenticated:
        data = {'authed': True,'username': request.user.username}
    else:
        data = {'authed': False}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
    return response
def gen_200(request):
    return HttpResponse('', status=200)
def _verifyRecaptcha(token, action):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': os.environ.get('RECAPTCHA_SECRET', ''),
        'response': token
    }
    data = urllib.parse.urlencode(payload).encode()
    req = urllib.request.Request(url, data=data)

    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    if (not result['success']) or (not result['action'] == action):
        return False
    return True

class domains(APIView):
    def get(self, request):
        data = [
            {
                'host': domain.host,
                'enable_hour': domain.enable_hours,
                'enable_week': domain.enable_week,
                'enable_months': domain.enable_month,
                'pk': domain.pk
            } for domain in Domain.objects.all()]
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
        return response
