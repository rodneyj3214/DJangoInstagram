# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from posts.forms import PostForm
from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'


# @login_required
# def list_post(request):
#     posts = Post.objects.all().order_by('-created')
#     # return HttpResponse('<br>'.join(contact))
#     return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def create_post(request):
    # return HttpResponse('<br>'.join(contact))
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    return render(request,
                  'posts/new.html',
                  {'form': form,
                   'user': request.user,
                   'profile': request.user.profile})
