from django.contrib import admin
from .models import Сategory, Product, AuthorСategory, ProductMaterial

# Cписок моделей администрации
admin.site.register(Сategory)
admin.site.register(Product)
admin.site.register(AuthorСategory)
admin.site.register(ProductMaterial)
