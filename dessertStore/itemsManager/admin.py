from django.contrib import admin
from .models import Category, Item
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "image_show"]

    def image_show(self, object):
        return mark_safe(f"<img src='{ object.image.url }' width='60' />")
    
    image_show.short_description = "Изображение"
