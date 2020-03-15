from ..models import Domain
from rest_framework.views import APIView
from django.http import HttpResponse
import json
import random

class domains(APIView):
    def get(self, request):
        data = [
            {
                'host': domain.host,
                'period': self._create_period(domain),
                'pk': domain.pk
            } for domain in Domain.objects.all()]
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
        return response
    
    def _create_period(self, domain):
        r = []
        if domain.enable_hours: r.append('hour')
        if domain.enable_week: r.append('days')
        if domain.enable_month: r.append('month')
        return r
