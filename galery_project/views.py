from django.shortcuts import render
from .models import Photo

def photo_list(request):

    photos = Photo.objects.all()
    print(photos)
    return render(request, 'galery_project/photo_list.html', {'photos': photos})
