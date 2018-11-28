from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from textEdit.models import Topic, Entry
from textEdit.forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


def index(request):
    """ The index page of the web application
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
    :param request:
    :return:
    """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'textEdit/topics.html', context)

def topic(request, topic_id):
    """ Overview of the topic selected
    :param request:
    :param topic_id:
        - id of the topic viewed
    :return:
        - request
        - template || /topic.html
        - context
    """
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'textEdit/topic.html', context)

@login_required
def new_topic(request):
    """ Page for creating a new topic
    :param request:
    :return:
        - Request
        - redirect to new topic
        - context
    """
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
    """ Page for adding a entry to the selected topic
    :param request:
    :param topic_id:
        - Topic where an entry is being added
    :return:
        - redirects || dest = textEdit:topic
    """
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
    """ A page where the entries can be changed (not deleted)
    :param request:
    :param entry_id:
    :return:
        - redirects || dest = textEdit:topic
    """
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

@login_required
def delete_topic(request, topic_id):
    """ deletes the topic selected
    :param request:
    :param topic_id:
    :return:
        - redirects || dest = textEdit:topics
    """
    topic = Topic.objects.get(id=topic_id)
    delete_topic = Topic.objects.get(pk=topic_id)

    if topic.owner != request.user:
        raise Http404
    else:
        delete_topic.delete()

    return HttpResponseRedirect(reverse('textEdit:topics'))


# TO DO:
#     - page for deleting entries
#     - page for seeing someone else his/her entries on the topic
#     - page overview topics
