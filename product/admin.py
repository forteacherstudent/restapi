from django.contrib import admin

from product.models import products

class productadmin(admin.ModelAdmin):
    list_display=('nm','desc')

admin.site.register(products,productadmin)



# Register your models here.
