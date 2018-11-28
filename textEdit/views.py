from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from textEdit.models import Topic, Entry
from textEdit.forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


def index(request):
    """ The index page of the web application
    This is the main page of the application, this will tell something about the website.
    It doesn't show any Topics/entries, unless its hardcoded.
    :Access:
        No Rights needed
    :param request:
        Request made by the routing
    :return:
        Template: textEdit/index.html || The index page
    """
    return render(request, 'textEdit/index.html')

@login_required
def topics(request):
    """ The Topic page of the web application
    This is the overview of the topics.
    :access:

    :param request:
    :return:
    """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'textEdit/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'textEdit/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('textEdit:topics'))
    context = {'form': form}
    return render(request, 'textEdit/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('textEdit:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'textEdit/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)

    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('textEdit:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'textEdit/edit_entry.html', context)
