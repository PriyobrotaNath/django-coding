from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView,product_list_View,create_product
from product.views.variant import VariantView, VariantCreateView, VariantEditView

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),

    path('products/', TemplateView.as_view(template_name='products/product_list.html', extra_context={
        'product': True
    }), name='product_list'),

    path('products/create/',create_product.as_view(), name='create_product'),

    path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),
]
