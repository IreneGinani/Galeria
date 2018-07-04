from django.shortcuts import render

def photo_list(request):
    return render(request, 'galery_project/photo_list.html', {})
