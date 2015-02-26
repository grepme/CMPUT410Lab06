from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect

from main.models import Link
from main.models import Tag

# Create your views here.


def index(request):
    """Display the bookmark index"""

    # Get the request context
    context = RequestContext(request)

    # Get all the links
    links = Link.objects.all()

    return render_to_response('main/index.html', {'links': links}, context)


def tags(request):
    """View all the tags"""

    # Get the context
    context = RequestContext(request)

    # Get all the tags
    tags = Tag.objects.all()

    return render_to_response('main/tags.html', {'tags': tags}, context)


def tag(request, tag_name):
    """View a specific tag"""

    # Get the context
    context = RequestContext(request)
    the_tag = Tag.objects.get(name=tag_name)
    links = the_tag.link_set.all()
    return render_to_response('main/index.html', {'links': links, 'tag_name': "#{}".format(tag_name)}, context)


def add_link(request):
    """Add a new link"""

    # Get the context
    context = RequestContext(request)
    if request.method == "POST":
        url = request.POST.get("url", "")
        tags = request.POST.get("tags", "")
        title = request.POST.get("title", "")

        # TODO: Add the link to the tags

        link = Link(title=title, url=url)
        link.save()
        for tag_new in tags.split(" "):
            try:
                t1 = Tag.objects.get(name=tag_new)
            except Tag.DoesNotExist:
                t1 = Tag(name=tag_new)
                t1.save()
            finally:
                link.tags.add(t1)
        link.save()

    return redirect(index)