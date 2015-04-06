from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from app.models import Comic
import mailchimp
MAILCHIMP_LIST_ID = 'dfd57ff352'
# Create your views here.

def index(request):
    comic = Comic.objects.latest('id')
    prev_id = comic.id - 1
    prev_url = ''
    try:
        prev_comic = Comic.objects.get(id=prev_id)
        prev_url = prev_comic.id
    except:
        pass
    return render(request, 'new_index.html',{'comic':comic, 'prev_url': prev_url})

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
    return render(request, 'new_index.html',{'comic':comic, 'prev_url': prev_url, 'next_url': next_url})

def archive(request):
    comics = Comic.objects.all()
    return render(request,'archive.html', {'comics':comics})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        print email
        m = mailchimp.Mailchimp('fb1d160cfea6730aad2dc1152842d944-us10')

        try:
            m.lists.subscribe(MAILCHIMP_LIST_ID, {'email':email})
            print "The email has been successfully subscribed"
        except mailchimp.ListAlreadySubscribedError:
            print "That email is already subscribed to the list"

        except mailchimp.Error, e:
            print 'An error occurred: %s - %s' % (e.__class__, e)
        return HttpResponseRedirect('/subscribe/')

    return render(request, 'subscribe.html')
