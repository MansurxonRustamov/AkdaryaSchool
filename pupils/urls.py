from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	path('', Home, name='home'),
	path('contact/', contactus, name='contact'),
	path('about/', About, name='about'),
	path('teachers/', TeacherDetail1, name='teachers'),
	path("rooms/", rooms, name="rooms"),
	path('contact/success/', ContactSuccess.as_view(), name='success'),
	path('dashboard/', dashPanel, name='dashboard'),
	path("dashboard/tableworks/", tablesWorks, name='table' ),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)