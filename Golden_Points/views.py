from django.shortcuts import render, redirect
from .form import PointForm
from .models import Point
from django.contrib.auth.decorators import login_required

@login_required
def add_point(request):
    if request.method == 'POST':
        form = PointForm(request.POST)
        if form.is_valid():
            point = form.save(commit=False)
            point.user = request.user
            point.save()
            return redirect('point_list')  # Redirect to a page that lists points
    else:
        form = PointForm()

    return render(request, 'golden_points/add_point.html', {'form': form})



@login_required
def points_list(request):
    return render(request, 'golden_points/points_list.html', )

  