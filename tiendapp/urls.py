from django.urls import path
from .views import v_index, v_cart, v_product_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', v_index, name = 'index'),
    path('cart', v_cart, name = 'cart'),
    path('product/code', v_product_detail, name = 'product_detail')
]

# Configuaracion para que se vean las imagenes solo en local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)