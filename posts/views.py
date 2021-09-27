# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post


@login_required
def list_post(request):
    posts = Post.objects.all().order_by('-created')
    # return HttpResponse('<br>'.join(contact))
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def create_post(request):
    # return HttpResponse('<br>'.join(contact))
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request,
                  'posts/new.html',
                  {'form': form,
                   'user': request.user,
                   'profile': request.user.profile})
