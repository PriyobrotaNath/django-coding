from django.views import generic

from product.models import Variant
from forms import ProductForm
from django.shortcuts import render,redirect



class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class product_list_View(generic.TemplateView):
    def product_list(request):
        products = Variant.objects.all()
        return render(request, 'product_list.html', {'products': products})
     

class create_product(generic.TemplateView):
    def create_product(request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('product_list')
        else:
            form = ProductForm()
        return render(request, 'create.html', {'form': form})