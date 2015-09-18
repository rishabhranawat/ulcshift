from django.conf.urls import url, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shifts.views import register

urlpatterns = patterns('',
    # ex: /polls/,
     url(r'^register/', register.as_view(), name = 'register'),
     
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()

'''
urlpatterns += patterns('',
 (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
 )
'''