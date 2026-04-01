from django.contrib import admin
from .models import Tour, TourImage, GalleryImage


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 3


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageInline]
    list_display = ('title', 'location', 'price')


@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')