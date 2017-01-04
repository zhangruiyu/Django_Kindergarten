from django.http import JsonResponse


def ok2json(data, *, token='', tel=''):
    return JsonResponse({'code': 200, 'token': token, 'tel': tel, "data": data})


def no2json(code):
    return JsonResponse({'code:': code[0], 'msg': code[1]})


def no2json(msg):
    return JsonResponse({'code:': 1000, 'msg': msg})

# def fail2json_parameterIsNone():
# from app.api_1_0.error import response_code
# return HttpResponse(response_code.error_parameter_isNone)
