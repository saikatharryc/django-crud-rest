from django.conf.urls import url

from.import views

urlpatterns = [
    # /videos/
    url(r'^$', views.index, name='index'),
    # /video/:id
    url(r'^(?P<videos_id>[0-9]+)/$', views.details, name='details'),
]
