from django.contrib import admin
from apps.models import Category, Product, ProductImages,User


class ProductImageInline(admin.StackedInline):
    model = ProductImages
    extra = 1

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ProductImageInline, ]
    list_display = ('name','price','quantity','category')
    search_fieds = ('name', 'price','quantity')


admin.site.register(Category)
admin.site.register(ProductImages)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username','first_name','last_name','phone','is_active')
    search_fields = ('username','phone')