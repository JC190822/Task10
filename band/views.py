from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Album

def index(request):
    albums = Album.objects.all()
    return render(request, 'band/index.html', {'albums': albums})

def album_detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    return render(request, 'band/album_detail.html', {'album': album})

from django.contrib.auth.decorators import login_required

@login_required
def restricted_view(request):
    # Get the authenticated user
    user = request.user

    # Example logic: Display a personalized message
    message = f"Welcome, {user.username}! This is the restricted view."

    # You can add more logic or queries related to the authenticated user here

    return render(request, 'band/restricted.html', {'message': message})
