from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from app.models import Comic
import mailchimp
MAILCHIMP_LIST_ID = 'dfd57ff352'
# Create your views here.

def index(request):
    comic = Comic.objects.latest('id')
    return HttpResponseRedirect('/%d/' %comic.id)


def comic(request, comic_id):
    print comic_id
    comic =  get_object_or_404(Comic, id=comic_id)
    prev_id = comic.id - 1
    prev_url = ''
    for prev_id in range(comic.id-1, 0, -1):
        try:
            prev_comic = Comic.objects.get(id=prev_id)
            prev_url = prev_comic.id
            break
        except:
            pass
    if prev_id == 0:
        prev_url = Comic.objects.latest('id').id         
    print "prev_id: ", prev_id
    print prev_url
    latest_comic = Comic.objects.latest('id').id
    next_id = 0
    next_url = ''
    comic_url = comic.image.url

    for next_id in range(comic.id+1,latest_comic+1,1):
        try:
            next_comic = Comic.objects.get(id=next_id)
            next_url = next_comic.id
            break
        except:
            pass

    if next_id == 0:
        for i in range(1,latest_comic+1):
            try:
                next_comic = Comic.objects.get(id=i)
                break
            except:
                pass
        next_url = next_comic.id
        next_id = next_comic

    print next_id

    return render(request, 'new_index.html',{'comic':comic, 'prev_url': prev_url, 'next_url': next_url})

def archive(request):
    comics = Comic.objects.all()
    return render(request,'new_archive.html', {'comics':comics})

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

def contact(request):
    print "fssgsg"
    if request.method == 'POST':
        print yes

        return HttpResponseRedirect('/')

    return render(request,'contact.html')

def dfg(request):
    return render(request,'123dfg.html')
