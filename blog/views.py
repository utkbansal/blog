from . import models
from django.views import generic


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = 'home.html'
    paginate_by = 4


class BlogDetailView(generic.DetailView):
    model = models.Entry
    template_name = 'post.html'