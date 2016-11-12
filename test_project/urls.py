from django.conf.urls import  url
from django.conf.urls import include
from Public_Cloud import views
from django.contrib import admin
from test_project import settings
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = [
	 url(r'^admin/', include(admin.site.urls)),
	 url(r'^Public_Cloud/', include('Public_Cloud.urls')),
	 url(r'^mypage/', include('mypage.urls'))
 ]