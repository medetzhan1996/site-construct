from django.urls import path
from . import views
app_name = 'shop-site'
urlpatterns = [
    path('<int:author>', views.IndexView.as_view(), name='index')
]
