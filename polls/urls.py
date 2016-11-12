from django.conf.urls import url
from polls import views
from test_project import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
		#url(r'^index/$',views.login),
		url(r'^index/$',views.index),
		url(r'^upload/$',views.upload),
		url(r'^play_file/$',views.play_file),
		#url(r'^viewFileList/$',views.viewFileList),
	    #url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),
         ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#if settings.DEBUG:
    #urlpatterns += patterns('',
        #url(r'^media/(?P<path>.*)$',
            #'django.views.static.serve',
            #{'document_root': settings.MEDIA_ROOT, }),
		#url(r'^upload/$',views.upload),
		#url(r'^from/$',views.Upload)
  #  )