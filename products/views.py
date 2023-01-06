from django.shortcuts import render, redirect
from products.models import Product, Category, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.

PAGINATION_LIMIT = 3

class ProductsCBV(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'products': kwargs['products'],
            'user': kwargs['user'],
            'pages': kwargs['pages']
        }

    def get(self, request, **kwargs):
        category_id = int(request.GET.get('category_id', 0))
        text = request.GET.get('text')
        page = int(request.GET.get('page', 1))

        if category_id:
            products = self.model.objects.filter(categories__in=[category_id])
        else:
            products = self.model.objects.all()

        if text:
            products = self.model.objects.filter(name__icontains=text)

        max_page = products.__len__() / PAGINATION_LIMIT

        if round(max_page) < max_page:
            max_page = round(max_page) + 1

        max_page = int(max_page)
        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        return render(
            request,
            self.template_name,
            context=self.get_context_data(
                products=products,
                user=None if request.user.is_anonymous else request.user,
                pages=range(1, max_page + 1)
            )
        )

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    queryset = Product.objects.all()
    pk_url_kwarg = 'id'
    context_object_name = 'product'


# def product_detail_view(request, id):
#     if request.method == 'GET':
#         product = Product.objects.get(id=id)
#
#         context = {
#             'product': product,
#             'reviews': product.review_set.all(),
#             'categories': product.categories.all(),
#             'review_form': ReviewCreateForm
#         }
#
#         return render(request, 'products/detail.html', context=context)
#
#     if request.method == 'POST':
#         product = Product.objects.get(id=id)
#         form = ReviewCreateForm(data=request.POST)
#
#         if form.is_valid():
#             Review.objects.create(
#                 author=request.user,
#                 product_id=id,
#                 text=form.cleaned_data.get('text')
#             )
#             return redirect(f'/products/{id}')
#         else:
#             return render(request, 'products/detail.html', context={
#                 'product': product,
#                 'reviews': product.review_set.all(),
#                 'categories': product.categories.all(),
#                 'review_form': form
#             })

class CategoriesCBV(ListView):
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'

# class ProductCreateView(CreateView):
#     form_class = ProductCreateForm
#     template_name = 'products/create.html'

    # queryset = Product.objects.all()

def product_create_view(request):
    if request.method == "GET":
        return render(request, 'products/create.html', context={
            'form': ProductCreateForm
        })

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                author=request.user,
                category=form.cleaned_data.get('category'),
                name=form.cleaned_data.get('name'),
                color=form.cleaned_data.get('color'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price', 0)
            )
            return redirect('/products/')
        else:
            return render(request, 'products/create.html', context={
                'form': form
            })

