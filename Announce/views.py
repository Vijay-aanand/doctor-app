from django.shortcuts import render
from .models import Announce  # Ensure this is the correct model name
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required

@login_required
def announce_list(request):
    announces = Announce.objects.all().order_by('-created_at')
    return render(request, 'Announce/announce_list.html', {'announces': announces})

@login_required
def json(request):
    data= list(Announce.objects.values())
    return JsonResponse(data, safe=False)
