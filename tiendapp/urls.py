from django.urls import path
from .views import v_index, v_cart, v_product_detail, v_add_to_cart, v_remove_from_cart, v_checkout
from django.conf import settings
from django.conf.urls.static import static
from .auth_views import v_sign_up, v_sign_up_create, v_sign_in, v_sign_out


urlpatterns = [
    path('', v_index, name = 'index'),
    path('cart', v_cart, name = 'cart'),
    path('product/<code>', v_product_detail, name = 'product_detail'),
    path('add_to_cart/<code>', v_add_to_cart, name = 'add_to_cart'),
    path('sign_up', v_sign_up, name = 'sign_up'),
    path("sign_up/create", v_sign_up_create, name="sign_up_create"),
    path("sign_in", v_sign_in, name="sign_in"),
    path("sign_out", v_sign_out, name="sign_out"),
    path("remove_from_cart/<code>", v_remove_from_cart, name="remove-from_cart"),
    path("checkout", v_checkout, name="checkout")
]

# Configuaracion para que se vean las imagenes solo en local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)