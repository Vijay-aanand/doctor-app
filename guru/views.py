from django.shortcuts import render, get_object_or_404
from .models import guru
from django.contrib.auth.decorators import login_required


@login_required
def guru_list(request):
    gurus = guru.objects.all()
    return render(request, 'guru/guru_list.html', {'gurus': gurus})



