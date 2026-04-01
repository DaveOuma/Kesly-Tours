from django.shortcuts import render
from rest_framework import viewsets
from .models import Tour, TourImage, GalleryImage
from .serializers import TourSerializer, TourImageSerializer, GalleryImageSerializer


def home(request):
    tours = [
        {
            "title": "Maasai Mara Safari",
            "location": "Maasai Mara",
            "price": "15000",
            "description": "Enjoy game drives, wildlife, and unforgettable safari experiences.",
            "images": [
                "images/mara1.jpg",
                "images/mara2.jpg",
            ],
        },
        {
            "title": "Diani Beach Escape",
            "location": "Diani",
            "price": "12000",
            "description": "Relax by the beach and enjoy the coastal beauty of Kenya.",
            "images": [
                "images/diani1.jpg",
                "images/diani2.jpg",
            ],
        },
        {
            "title": "Amboseli Adventure",
            "location": "Amboseli",
            "price": "18000",
            "description": "See elephants and amazing views of Mount Kilimanjaro.",
            "images": [
                "images/amboseli1.jpg",
            ],
        },
    ]

    gallery = [
        {
            "title": "Safari Moments",
            "image": "images/mara1.jpg",
            "caption": "Discover the wild",
        },
        {
            "title": "Beach Experience",
            "image": "images/diani1.jpg",
            "caption": "Feel the ocean breeze",
        },
        {
            "title": "Adventure Travel",
            "image": "images/amboseli1.jpg",
            "caption": "Travel with KESLY TOURS AND SAFARIS",
        },
    ]

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