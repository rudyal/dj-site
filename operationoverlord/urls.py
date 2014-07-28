from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User, Group
from polls import views
from tastypie.api import Api
from rest_framework import viewsets, routers
from polls.models import PictureObject
from polls import api

# v1_api = Api(api_name='v1')
# v1_api.register(UserResource())
# v1_api.register(PicResource())
# v1_api.register(TagResource())

admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'pics', views.PicViewSet)



urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	#url(r'^api/', include(v1_api.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/pic/$', api.PictureObjectList.as_view()),
	url(r'^api/pic/(?P<pk>[0-9]+)/$', api.PictureObjectDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	# static files (images, css, javascript, etc.)
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT}))
