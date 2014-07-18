from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    # ex: /polls/
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	url(r'^addcontent/$', views.CreatePicObModel, name='CreatePicObModel'),
	url(r'^viewcontent/$', views.ViewPicOb, name='ViewPicOb'),
	url(r'^viewer/$', views.Viewer, name='Viewer'),
)