# otp/urls.py

from django.contrib import admin
from django.urls import path, include  # Include 'include' to use 'Menu' app's urls
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from onetime import views  # Import your views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('onetime/',include('onetime.urls')),
    path('announce/', include('Announce.urls')),  # Include 'announce' app urls
    path('menu/', include('Menu.urls')),  # Include 'Menu' app urls
    path('json_ot/',views.json_ot,name='jason_ot'),
    path('mcq/',include('MCQ.urls')),
    path('golden_points/', include('Golden_Points.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include the authentication URLs
    path('guru/',include('guru.urls')),
    path('Video/',include('Video.urls'))

]

# Add media URL serving in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
