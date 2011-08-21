from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from blog.models import Post

urlpatterns = patterns('',
    (r'^$', ListView.as_view(
        queryset=Post.live.all(),
        context_object_name='latest_blog_list',
        template_name='blog/index.html',
        paginate_by=3)),
    (r'^(?P<pk>\d+)/$',
     DetailView.as_view(
        model=Post,
        template_name='blog/post.html')),
)

