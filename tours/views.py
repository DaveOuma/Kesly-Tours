from django.shortcuts import render
from rest_framework import viewsets
from .models import Tour, TourImage, GalleryImage
from .serializers import TourSerializer, TourImageSerializer, GalleryImageSerializer


def home(request):
    tours = Tour.objects.prefetch_related('images').all().order_by('-created_at')
    gallery = GalleryImage.objects.all().order_by('-uploaded_at')

    return render(request, 'tours/home.html', {
        'business_name': 'KESLY TOURS AND SAFARIS',
        'phone': '+254704509111',
        'email': 'jerzenterprises@gmail.com',
        'tours': tours,
        'gallery': gallery,
    })


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.prefetch_related('images').all()
    serializer_class = TourSerializer


class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer