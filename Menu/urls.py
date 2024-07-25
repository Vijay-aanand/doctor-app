from django.urls import path


from . import views
  
urlpatterns = [
    path('', views.menu, name='menu'),
    path('explore_plans/', views.explore_plans, name='explore_plans'),
    path('subscription/', views.subscription, name='subscription'),
    path('qbank/', views.qbank, name='qbank'),
    path('test/', views.test, name='test'),
    path('folders/', views.folder_list, name='folder_list'),
    path('videos/<int:video_id>/folders/', views.video_folders, name='video_folders'),
    path('folders/<int:folder_id>/videos/', views.folder_videos, name='folder_videos'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('help_center/', views.help_center, name='help_center'),
    path('explore_plans/json_plan/', views.json_plan, name='json_plan'),
    path('subscription/json_subscription/', views.json_subscription, name='json_subscription'),
    path('videos/json_video/', views.json_video, name='json_video'),
    path('qbank/json_qbank/', views.json_qbank, name='json_qbank'),
    path('test/json_test/', views.json_test, name='json_test'),
    path('videos/save/<int:video_id>/', views.save_video, name='save_video'),
    path('menu/folders/1/videos/saved', views.saved_videos, name='saved_videos'),

]
