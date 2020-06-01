from django.shortcuts import render

from .forms import URLForm
from .models import MiniURL
from .utils import generate


def hello_world(request):
    form = URLForm(request.POST or None)

    if form.is_valid():
        url = form.cleaned_data['url']
        author = form.cleaned_data['author']
        code = generate(6)

        m_url = MiniURL(url=url, author=author, code=code)
        m_url.save()

        sent = True

    return render(request, 'mini_url/form.html', locals())
