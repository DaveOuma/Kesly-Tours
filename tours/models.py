from django.db import models


class Tour(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='tours/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.tour.title


class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title