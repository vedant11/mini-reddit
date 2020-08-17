from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Post


# generic django views:


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Post
    template_name = "polls/details.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Post
    template_name = "polls/results.html"


def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        selected_post = post.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {"post": post, "error_message": "You didnt select any choice"},
        )
    else:
        selected_post.votes += 1
        selected_post.save()
        return HttpResponseRedirect(reverse("polls:results", args=[post_id]))