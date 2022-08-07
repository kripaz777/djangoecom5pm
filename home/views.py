from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class Base(View):
	context = {}

class HomeView(Base):
	def get(self,request):
		self.context['categories'] = Category.objects.all()
		self.context['subcategories'] = SubCategory.objects.all()
		self.context['sliders'] = Slider.objects.all()
		self.context['ads'] = Ad.objects.all()
		self.context['brands'] = Brand.objects.all()
		self.context['hot_product'] = Product.objects.filter(labels = 'hot')
		self.context['new_product'] = Product.objects.filter(labels = 'new')
		self.context['customers'] = Customer.objects.all()
		return render(request,'index.html',self.context)

class CategoryView(Base):
	def get(self,request,slug):
		ids = Category.objects.get(slug = slug).id
		self.context['category_product'] = Product.objects.filter(category_id = ids)

		return render(request,'category.html',self.context)

class DetailView(Base):
	def get(self,request,slug):
		self.context['product_detail'] = Product.objects.filter(slug = slug)
		self.context['categories'] = Category.objects.all()
		self.context['brands'] = Brand.objects.all()
		all_brand = []
		for i in Brand.objects.all():
			ids = Brand.objects.get(name = i).id
			count = Product.objects.filter(brand = ids).count()
			all_brand.append({'product_count':count,'ids':ids})
			self.context['counts'] = all_brand

		return render(request,'product-detail.html',self.context)


class SearchView(Base):
	def get(self,request):
		query = request.GET.get('query')
		print(query)
		if not query:
			return redirect('/')
		self.context['search_product'] = Product.objects.filter(name__icontains = query)
		return render(request,'search.html',self.context)
