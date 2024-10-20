from django.contrib import admin

from store.models import NetworkEntity, Product


@admin.action(description="Обнулить задолжность")
def make_published(modeladmin, request, queryset):
    queryset.update(debt=0.0)


@admin.register(NetworkEntity)
class NetworkEntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'level', 'parent_entity', 'debt', 'created_at',)
    list_filter = ('city',)
    search_fields = ('name',)
    actions = (make_published,)
    list_display_links = ('parent_entity',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'supplier',)
    list_filter = ('supplier', 'release_date',)
    search_fields = ('name', 'supplier',)
