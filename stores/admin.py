from django.contrib import admin
from .models import Store
from django.utils.html import format_html

# Register your models here.


class StoreAdmin(admin.ModelAdmin):
	list_display=['id','name','description']
	search_fields = ['name','description']
	list_filter = ['added']
	list_display_links = ['name']
	list_editable=['description']

	class Meta:
		model = Store

admin.site.register(Store,StoreAdmin)