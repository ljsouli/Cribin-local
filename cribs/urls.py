from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^subscribe/',views.subscribe, name='subscribe'),
    url(r'^home/',views.home, name='home'),
    url(r'^browse/',views.browse, name='browse'),
    url(r'^next_crib/',views.nextCrib, name='next_crib'),

    #url(r'^$', views.index, name='index'),
    
    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

