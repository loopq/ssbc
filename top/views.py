import json

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http.response import HttpResponse, JsonResponse
from .models import KeywordLog, HashLog


# Create your views here.


@cache_page(600)
def index(request):
    d = {
        'top_keyword_daily': KeywordLog.objects.top_daily(),
        'top_hash_daily': HashLog.objects.top_daily(),
    }
    return render(request, 'top.html', d)


@cache_page(600)
def jsonindex(request):
    d = {
        'top_keyword_daily': list(KeywordLog.objects.top_daily()),
        'top_hash_daily': list(HashLog.objects.top_daily()),
    }
    return returnResult('success', 'success', d)


def json_log(request):
    log_type = request.GET.get('type')
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if not ip:
        ip = request.META.get('HTTP_X_REAL_IP', '')
    if log_type == 'keyword':
        keyword = request.GET['keyword'].strip()[:100]
        KeywordLog.objects.create(keyword=keyword, ip=ip)
    elif log_type == 'hash':
        try:
            hash_id = int(request.GET['hash'])
            hash_name = request.GET['name']
        except ValueError:
            return HttpResponse('invalid')
        HashLog.objects.create(hash_id=hash_id, ip=ip, hash_name=hash_name)
    return HttpResponse('ok')


def json_into_db(log_type, keyword='', hash_id='', hash_name=''):
    if log_type == 'keyword':
        KeywordLog.objects.create(keyword=keyword, ip='')
    elif log_type == 'hash':
        HashLog.objects.create(hash_id=hash_id, ip='', hash_name=hash_name)


def returnResult(status, msg, data):
    result = {}
    result['status'] = status
    result['msg'] = msg
    result['data'] = data
    return HttpResponse(json.dumps(result))
