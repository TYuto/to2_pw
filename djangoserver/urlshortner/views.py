from .models import Url
from rest_framework.views import APIView
from django.http import HttpResponse
import json
import uuid
class urls(APIView):
    def get(self, request):
        if request.user == None:
            try:
                pk = request.session['uuid']
            except KeyError:
                pk = uuid.uuid4
                request.session['uuid'] = pk
            urls = Url.objects.filter(tempuser_id=pk)
        else:
            urls = Url.objects.filter(user=request.user.id)
        data = [
            {
                'original_url': url.original_url,
                'shorten_url': url.shorten_url,
                'validiry_period': url.validity_period,
                'expiration_date': url.expiration_date.timestamp()
            } for url in urls]
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
        return response