from django.http import JsonResponse


def pizzaview(request):
    return JsonResponse(
        {"message": "Hello Pizza Mizza"}
    )
