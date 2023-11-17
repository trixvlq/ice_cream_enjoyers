from django.contrib import admin
from .models import *
class IceCreamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
admin.site.register(IceCream,IceCreamAdmin)
admin.site.register(Category)
admin.site.register(Bag)