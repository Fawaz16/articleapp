from pydoc_data import topics
from django.shortcuts import render
from. models import Business,Weekend,Topic


# Create your views here.
def home(request):
    '''render home page'''
    my_topics=Topic.objects.all()
    new_topic=Business.objects.all()
    weekend_topic=Weekend.objects.all()
    # opinion=Opinion.objects.all()
    return render(request, 'index.html', {'topics':my_topics, 'topic':new_topic, 'weekend':weekend_topic})

def content(request,post_id):
    ''''render the content page'''
    print(post_id)
    # headlines=content_1.objects.all()[0]
    topics=Topic.objects.get(id=post_id)
    topic1=Business.objects.get(id=post_id)
    # topic2=Weekend.objects.get(id=post_id)
    return render(request,'content.html',{'topic':topics,'topics':topic1})
def article(request,post_id):
    ''''render the content page'''
    print(post_id)
    topic1=Business.objects.get(id=post_id)
    # topic2=Weekend.objects.get(id=post_id)
    return render(request,'article.html',{'topics':topic1})

def weekend(request,post_id):
    ''''render the content page'''
    print(post_id)
    topic1=Weekend.objects.get(id=post_id)
    # topic2=Weekend.objects.get(id=post_id)
    return render(request,'weekend.html',{'topics':topic1})
