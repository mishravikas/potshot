from django.shortcuts import render, get_object_or_404
from app.models import Comic

# Create your views here.

def index(request):
    comic = Comic.objects.latest('id')
    prev_id = comic.id - 1
    prev_comic = Comic.objects.get(id=prev_id)
    return render(request, 'index.html',{'comic':comic, 'prev_url': prev_comic.id})

def comic(request, comic_id):
    print comic_id
    comic =  get_object_or_404(Comic, id=comic_id)
    prev_id = comic.id - 1
    next_id = comic.id + 1
    prev_url = ''
    next_url = ''
    comic_url = comic.image.url
    try:
        prev_comic = Comic.objects.get(id=prev_id)
        prev_url = prev_comic.id
    except:
        pass

    try:
        next_comic = Comic.objects.get(id=next_id)
        print "HERE"
        next_url = next_comic.id
    except:
        pass
    print comic.image.url
    return render(request, 'index.html',{'comic':comic, 'prev_url': prev_url, 'next_url': next_url})

def archive(request):
    comics = Comic.objects.all()
    return render(request,'archive.html', {'comics':comics})
