from django.db import models
from django.conf import settings


# Базовый абстрактный класс
class ItemBase(models.Model):
    title = models.CharField(max_length=180)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# Список категории
class Сategory(ItemBase):
    pass

    class Meta:
        db_table = "categories"


# Список категориев выбранные пользователями
class AuthorСategory(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(Сategory,
                                 related_name='authors_category',
                                 on_delete=models.CASCADE)

    class Meta:
        db_table = "author_categories"

    def __str__(self):
        return self.category.title


# материалы
class Material(ItemBase):
    pass

    class Meta:
        db_table = "materials"


# Связь материала с продуктом М-М
class ProductMaterial(models.Model):
    material = models.ForeignKey(Material,
                                 related_name='rel_material',
                                 on_delete=models.CASCADE)
    product = models.ForeignKey('Product',
                                related_name='rel_product',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        db_table = "products_materials"

    def __str__(self):
        return f'{self.material} rel {self.product}'


# список товаров
class Product(ItemBase):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    KIND_CHOICES = [
        ('normal', 'Обычный'),
        ('image_select', 'Выбор изображения'),
        ('text_input', 'Набор текста')
    ]
    file = models.FileField(upload_to='images', blank=True)
    author_category = models.ForeignKey(AuthorСategory,
                                        related_name='products_auth_category',
                                        on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    price_old = models.DecimalField(max_digits=10, decimal_places=0,
                                    blank=True, null=True)
    is_top = models.BooleanField(default=False)
    kind = models.CharField(
        max_length=12,
        choices=KIND_CHOICES,
        default='normal'
    )
    classes = models.CharField(max_length=180, blank=True)
    materials = models.ManyToManyField(Material,
                                       through='ProductMaterial',
                                       related_name='rel_materials')
    is_select_material = models.BooleanField(default=False)

    class Meta:
        db_table = "products"
