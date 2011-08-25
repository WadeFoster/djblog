from django.conf.urls.defaults import *
from django.views.generic import ListView
from blog.models import Post
from blog import views

urlpatterns = patterns('',
    (r'^$', ListView.as_view(
        queryset=Post.live.all(),
        context_object_name='latest_blog_list',
        template_name='blog/index.html',
        paginate_by=3)),
    url(r'^(?P<slug_from_url>[-\w]+)/$', views.view_post, name='view_post'),
)

