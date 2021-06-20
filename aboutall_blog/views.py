from django.shortcuts import render, get_object_or_404

from aboutall_blog.models import Aboutall


def all_blogs(request):
#    posts = Aboutall.objects.all()
    posts = Aboutall.objects.order_by('-post_create_at') # [:5] ordered bu date and showing just 5 posts
    return render(request, 'aboutall_blog/all_blogs.html', context={'posts': posts}) # 'posts' goas to html file

def detail(request, post_id):
    blog_post = get_object_or_404(Aboutall, pk=post_id) # pk - primary key
    return render(request, 'aboutall_blog/detail.html', context={'blog_post': blog_post})
