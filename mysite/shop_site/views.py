from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Сategory
# List views


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        author = get_object_or_404(User, id=self.kwargs['author'])
        kwargs.setdefault("author", author)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.kwargs['author']
        context['categories'] = Сategory.objects.filter(author=author).all()
        return context
