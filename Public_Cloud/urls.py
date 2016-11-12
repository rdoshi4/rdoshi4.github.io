from django.conf.urls import url
from Public_Cloud import views
from test_project import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [	
		url(r'^register/$',views.register),
		url(r'^login/$',views.login),
		url(r'^upload/$',views.upload),
		url(r'^play_file/$',views.play_file),
		url(r'^logout/$',views.logout),
		]
		