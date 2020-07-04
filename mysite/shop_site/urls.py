from django.urls import path
from . import views
app_name = 'shop-site'
urlpatterns = [
    path('<int:author>', views.IndexView.as_view(), name='index'),
    path('<int:author>/<int:category>', views.IndexView.as_view(),
         name='index'),
    path('card/<int:author>/<pk>', views.ProductDetailView.as_view(),
         name='product_detail')
]
