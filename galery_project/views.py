from django.shortcuts import render
from .models import Photo
import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAIULCLLPCS7NY223A'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'galeria-fotos'


def photo_list(request):


    file_name = 'images-to-upload/' + request.GET['file-input'];
    data = open(file_name, 'rb')
    s3 = boto3.resource(
        's3', 
         aws_access_key_id=ACCESS_KEY_ID,
         aws_secret_access_key=ACCESS_SECRET_KEY,
         config=Config(signature_version='s3v4')
    )

# Image Uploaded

    s3.Bucket(BUCKET_NAME).put_object(Key=file_name, Body=data, ACL='public-read')
   
    name = "https://s3-sa-east-1.amazonaws.com/" + BUCKET_NAME + "/images-to-upload/" + request.GET['file-input']
    photo = Photo(name=name)
    photo.save()


    photos = Photo.objects.all()
    print(photos)
    return render(request, 'galery_project/photo_list.html', {'photos': photos})

def photo_upload(request):

	return render(request, 'galery_project/upload_photo.html')

