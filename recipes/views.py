from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')
    # return JsonResponse({'message': msg})
    # return HttpResponse(msg)

def sobre(request):
    return render(request, 'sobre.html')