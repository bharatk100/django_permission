from django.shortcuts import render
from .models import blog
from .forms import BlogForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.contrib.auth.decorators import permission_required


def home(request):
    return render(request, 'app1/home.html')


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "app1/create_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = blog.objects.all()

    return render(request, "app1/list_view.html", context)


# after updating it will redirect to detail_View
@permission_required("app1.view_blog")
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = blog.objects.get(id=id)

    return render(request, "app1/detail_view.html", context)


# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(blog, id=id)

    # pass the object as instance in form
    form = BlogForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "app1/update_view.html", context)


# user1 does not have permission to view this delete view, so user1 redirect to login view
@permission_required("app1.view_blog")
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(blog, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "app1/delete_view.html", context)
