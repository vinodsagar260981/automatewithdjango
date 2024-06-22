from django.contrib import admin
from .models import CompressImage
from django.utils.html import format_html

# Register your models here.
class CompressImageAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.compressed_img.url}" width="40" height="40" >')
    
    def original_size(self, obj):
        return format_html(f'{obj.original_img.size / (1024 * 1024):.2f} MB ')
    
    def compressed_size(self, obj):
        size_in_mb = obj.compressed_img.size / (1024 * 1024)
        
        if size_in_mb > 1:
            return format_html(f'{size_in_mb:.2f} MB')
        else:
            size_in_kb = obj.compressed_img.size / 1024
            return format_html(f'{size_in_kb:.2f} kb')


    list_display = ('user', 'thumbnail', 'original_size', 'compressed_size', 'compressed_at')


admin.site.register(CompressImage, CompressImageAdmin)