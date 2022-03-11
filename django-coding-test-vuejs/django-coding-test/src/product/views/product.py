from django.views import generic
from product.models import Variant, Product, ProductVariantPrice


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        productvariantprice = ProductVariantPrice.objects.filter().values('id', 'product__title', 'product_variant_one', 'product_variant_two', 'product_variant_three', 'price', 'created_at', 'updated_at')
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        context['productvariantprice'] = list(productvariantprice.all())
        return context





