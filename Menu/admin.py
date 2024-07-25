from django.contrib import admin
from .models import Plan,Subscription,Video,QBank,Test,Folder

# Register your models here.
admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(QBank)
admin.site.register(Test) 
class VideoAdmin(admin.ModelAdmin):
    list_display=['title','folder','url']
admin.site.register(Folder)
admin.site.register(Video,VideoAdmin)



