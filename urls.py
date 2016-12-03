from django.conf.urls import url
from mypage import views
from test_project import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [	
		url(r'^about/$',views.about),
		url(r'^info/$',views.info)
		]