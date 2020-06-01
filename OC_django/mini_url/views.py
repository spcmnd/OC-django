from django.shortcuts import render, redirect, Http404

from .forms import URLForm
from .models import MiniURL
from .utils import generate


def generate_redirection(request):
    form = URLForm(request.POST or None)

    if form.is_valid():
        url = form.cleaned_data['url']
        author = form.cleaned_data['author']
        code = generate(6)

        m_url = MiniURL(url=url, author=author, code=code)
        m_url.save()

        sent = True

    return render(request, 'mini_url/form.html', locals())


def redirect_user(request, code):
    if not code:
        raise Http404

    url = MiniURL.objects.get(code=code)
    url.redirect_access += 1
    url.save()

    return redirect(url.url)


def redirection_list(request):
    redirections = MiniURL.objects.order_by('-redirect_access')

    return render(request, 'mini_url/list.html', locals())
