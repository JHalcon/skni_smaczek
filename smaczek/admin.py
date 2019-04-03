from django.contrib import admin

# Register your models here.
from smaczek.models import ProductType, Product


class ProductTypeAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
