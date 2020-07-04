from django.db import models
from django.conf import settings

# Базовый класс


class ItemBase(models.Model):
    title = models.CharField(max_length=180)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# Список категории
class Сategory(ItemBase):
    pass

    class Meta:
        db_table = "categories"


# список товаров
class Product(ItemBase):
    KIND_CHOICES = [
        ('normal', 'Обычный'),
        ('image_select', 'Выбор изображения'),
        ('text_input', 'Набор текста')
    ]
    file = models.FileField(upload_to='images', blank=True)
    category = models.ForeignKey(Сategory,
                                 related_name='products_category',
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_old = models.DecimalField(max_digits=6, decimal_places=2)
    is_top = models.BooleanField(default=False)
    kind = models.CharField(
        max_length=12,
        choices=KIND_CHOICES,
        default='normal'
    )

    class Meta:
        db_table = "products"
