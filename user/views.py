# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from error.response_code import error_UserExist
from u import ok2json, no2json
from user.models import User
from django.conf import settings
from django.core.cache import cache

def auth_login(request):
    print(request)
    return HttpResponse('fdfad')


@csrf_exempt
@require_POST
def login(request):
    print(request.POST)
    post = request.POST
    value = cache.get(post['tel'])
    print(value)
    cache.set(post['tel'],post['tel'])
    value = cache.get(post['tel'])
    print(value)

    has_key(request, ('tel', 'pwd'))
    if not post['tel'] or not post['pwd']:
        return no2json('手机号或密码不能为空')
    try:
        user = User.objects.get(tel=post['tel'])
        if user:
            check_password(post['pwd'], user.password)
            print(User.objects.get(tel=post['tel']).password)
            return no2json(error_UserExist)
    except User.DoesNotExist:
        User.createUser(post['tel'], post['pwd'])
        return ok2json('创建成功')


@csrf_exempt
@require_POST
def register(request):
    print(request.POST)
    post = request.POST
    has_key(request, ('tel', 'pwd'))
    if not post['tel'] or not post['pwd']:
        return no2json('手机号或密码不能为空')
    try:
        if User.objects.get(tel=post['tel']):
            print(User.objects.get(tel=post['tel']).password)
            return no2json(error_UserExist)
    except User.DoesNotExist:
        User.createUser(post['tel'], post['pwd'])
        return ok2json('创建成功')


def logout(request, key):
    if not request.POST.has_key(key):
        return ""


def has_key(request, arguments=()):
    if len(arguments) > 0:
        for argumentKey in arguments:
            if argumentKey not in request.POST:
                fail = {'code': 0, 'msg': '参数不完整:' + argumentKey}
                raise Exception(fail)

    return request


def password_change(request):
    return None


def password_change_done(request):
    return None


def password_reset(request):
    return None


def password_reset_done(request):
    return None


def password_reset_complete(request):
    return None


def password_reset_confirm(request):
    return None
