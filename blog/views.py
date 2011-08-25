from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Post


def view_post(request, slug_from_url):
    post = get_object_or_404(Post, slug=slug_from_url)
    return render_to_response('blog/post.html',
        RequestContext( request, locals() ) )

