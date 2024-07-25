from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Plan, Subscription, Video, QBank, Test, Folder,SavedVideo
from django.http import JsonResponse
import json
from .form import VideoUploadForm

@login_required
def menu(request):
    return render(request, 'menu/menu.html')

@login_required
def explore_plans(request):
    plans= Plan.objects.all()
    print(plans)
    return render(request, 'menu/plan.html',{'plans': plans})  

@login_required
def subscription(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'menu/subscription.html', {'subscriptions': subscriptions})

@login_required
def qbank(request):
    qbanks = QBank.objects.all()
    return render(request, 'menu/qbank.html', {'qbanks': qbanks})
                                                              
@login_required
def test(request):
    tests = Test.objects.all()
    return render(request, 'menu/test.html', {'tests': tests})

@login_required
def videos(request):
    videos = Video.objects.all()
    return render(request, 'menu/video.html', {'videos': videos})

@login_required
def terms_and_conditions(request):
    return render(request, 'menu/terms_and_conditions.html')

@login_required
def help_center(request):
    return render(request, 'menu/help_center.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def json_plan(request):
    data = list(Plan.objects.values())
    return JsonResponse(data, safe=False)

@login_required
def json_subscription(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    data = [{
        'plan': subscription.plan.name,
        'start_date': subscription.start_date,
        'end_date': subscription.end_date
    } for subscription in subscriptions]
    return JsonResponse(data, safe=False)

@login_required
def json_video(request):
    data = list(Video.objects.values())
    return JsonResponse(data, safe=False)

@login_required
def json_qbank(request):
    data = list(QBank.objects.values())
    return JsonResponse(data, safe=False)

@login_required
def json_test(request):
    data = list(Test.objects.values())
    return JsonResponse(data, safe=False)

@login_required
def video_folders(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    folders = Folder.objects.filter(videos=video)
    return render(request, 'menu/video_folders.html', {'video': video, 'folders': folders})

@login_required
def folder_videos(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    videos = folder.videos.all()
    return render(request, 'menu/folder_videos.html', {'folder': folder, 'videos': videos})

@login_required
def folder_list(request):
    folders = Folder.objects.all()
    return render(request, 'menu/folder_list.html', {'folders': folders})


@login_required
def save_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    SavedVideo.objects.get_or_create(user=request.user, video=video)
    return redirect('saved_video_list')

    # Assuming each video belongs to a folder, and you have a way to get the folder_id
   # Change this according to your actual model relations

    # Redirect to the folder_videos page
 

@login_required
def saved_videos(request):
    saved_videos = SavedVideo.objects.filter(user=request.user)
    return render(request, 'menu/saved_videos.html', {'saved_videos': saved_videos})


