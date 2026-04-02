from django.shortcuts import render
from rest_framework import viewsets
from .models import Tour, TourImage, GalleryImage
from .serializers import TourSerializer, TourImageSerializer, GalleryImageSerializer


def home(request):
    tours = [
        {
            "title": "Maasai Mara Safari",
            "location": "Maasai Mara",
            "price": "37000",
            "description": "Enjoy game drives, wildlife, and unforgettable safari experiences.",
            "images": [
                "images/images1.jpg",
                "images/images2.jpg",
            ],
        },
        {
            "title": "Diani Beach Escape",
            "location": "Diani",
            "price": "30000",
            "description": "Relax by the beach and enjoy the coastal beauty of Kenya.",
            "images": [
                "images/download3.jpg",
                "images/view-horse-drinking-water-from-tree_118919-4884.jpg.jpg",
            ],
        },
        {
            "title": "Amboseli Adventure",
            "location": "Amboseli",
            "price": "35000",
            "description": "See elephants and amazing views of Mount Kilimanjaro.",
            "images": [
                "images/pexels-droneafrica-13234382.jpg",
            ],
        },
    ]

    gallery = [
        {
            "title": "Safari Moments",
            "image": "images/pexels-droneafrica-13234382.jpg",
            "caption": "Discover the wild",
        },
        {
            "title": "Beach Experience",
            "image": "images/pexels-490714164-28157155.jpg",
            "caption": "Feel the ocean breeze",
        },
        {
            "title": "Adventure Travel",
            "image": "images/pexels-490714164-28157155.jpg",
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