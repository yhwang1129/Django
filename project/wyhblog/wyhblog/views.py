from django.http import HttpResponse, JsonResponse


def test_cors(request):

    return JsonResponse({'msg': 'CORS is ok'})