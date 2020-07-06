from django.shortcuts import redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.mixins import LoginRequiredMixin
from shop_site.models import AuthorСategory, Product
from shop_site.forms import CategoryForm


# Главная страница менеджера
class IndexView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'manager/index.html'
    category_form_class = CategoryForm
    auth_categories = None
    products = None

    def get(self, request, *args, **kwargs):
        self.auth_categories = AuthorСategory.objects.filter(
            author=request.user.id).all()
        self.products = Product.objects.filter(
            is_top=True, author=request.user.id)[:12]
        return self.render_to_response(
            {'auth_categories': self.auth_categories,
             'products': self.products,
             'category_form': self.category_form_class()})

    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST
        }
        category_form = self.category_form_class(**form_args)
        if category_form.is_valid():
            category_form.save()
            return redirect('manager:index')
        return self.render_to_response(
            {'category_form': self.category_form,
             'products': self.products,
             'auth_categories': self.auth_categories})
