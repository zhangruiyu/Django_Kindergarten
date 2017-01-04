from django.http import JsonResponse


def handler400(error):
    return JsonResponse(error)
